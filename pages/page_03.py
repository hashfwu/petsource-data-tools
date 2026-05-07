import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.efficientnet import preprocess_input
import json
import pandas as pd
import os
from pathlib import Path

st.set_page_config(page_title="Analizador de Emociones", page_icon="😊")

st.title("😊 Analizador de Emociones para Mascotas")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("models/dog_emotion_classifier.h5")

try:
    model = load_model()
    model_ready = True
except Exception as e:
    st.error(f"Error cargando modelo: {e}")
    model_ready = False

def preprocess_image(image, target_size=(300, 300)):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    img = image.resize(target_size, Image.Resampling.LANCZOS)
    img_array = np.array(img, dtype=np.float32)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def load_training_history():
    """Carga el historial de entrenamiento"""
    history_path = "models/model_metrics/model_training_history.json"
    if os.path.exists(history_path):
        with open(history_path, 'r') as f:
            return json.load(f)
    return None

@st.cache_data
def load_classification_report():
    """Carga el reporte de clasificación"""
    report_path = "models/model_metrics/classification_report.json"
    if os.path.exists(report_path):
        with open(report_path, 'r') as f:
            return json.load(f)
    return None

@st.cache_data
def load_confusion_matrix():
    """Carga la matriz de confusión"""
    matrix_path = "models/model_metrics/confusion_matrix.csv"
    if os.path.exists(matrix_path):
        return pd.read_csv(matrix_path, index_col=0)
    return None

@st.cache_data
def load_training_log():
    """Carga el log de entrenamiento"""
    log_path = "models/model_metrics/training_log.csv"
    if os.path.exists(log_path):
        return pd.read_csv(log_path)
    return None

tab_prediccion, tab_metricas = st.tabs(["🔮 Predicción en Vivo", "📊 Métricas del Modelo"])
image = None

with tab_prediccion:
    st.markdown("### Sube o toma una foto de tu mascota")
    
    col_camara, col_subida = st.columns(2)
    
    image = None
    
    with col_camara:
        img = st.camera_input("📸 Tomar foto", key="camera_input")
        if img:
            image = Image.open(img)
    
    with col_subida:
        img = st.file_uploader("📁 Subir imagen", type=["jpg", "jpeg", "png"], key="file_uploader")
        if img:
            image = Image.open(img)
    
    if image and model_ready:
        with st.spinner("🔬 Analizando emociones..."):
            img_array = preprocess_image(image, tuple((300, 300)))
            predictions = model.predict(img_array, verbose=0)[0]
            emociones = ["Enojado 😠", "Triste 😢", "Feliz 😊", "Relajado 😐"]
            
            st.subheader("📊 Resultado del análisis")
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(image, caption="Imagen analizada", use_container_width=True)
            
            with col2:
                emotion_idx = np.argmax(predictions)
                confidence = predictions[emotion_idx]
                
                st.metric(
                    label="🎯 Emoción detectada",
                    value=f"{emociones[emotion_idx]}",
                    delta=f"Confianza: {confidence:.1%}"
                )
                
                st.markdown("---")
                st.write("### Distribución de emociones")
                
                # Colores para cada emoción
                colores = {
                    "Enojado 😠": "#ff4444",
                    "Triste 😢": "#4444ff",
                    "Feliz 😊": "#00cc44",
                    "Relajado 😐": "#ffaa00"
                }
                
                for emo, prob in zip(emociones, predictions):
                    st.progress(float(prob), text=f"{emo}: {prob:.1%}")
                
                with st.expander("📈 Ver probabilidades exactas"):
                    for emo, prob in zip(emociones, predictions):
                        st.write(f"- {emo}: {prob:.4f} ({prob:.2%})")

with tab_metricas:
    st.markdown("### 📈 Rendimiento del Modelo de Clasificación de Emociones")
    
    # Cargar todos los datos
    history = load_training_history()
    report = load_classification_report()
    confusion = load_confusion_matrix()
    training_log = load_training_log()
    
    # Verificar si hay datos
    if not any([history, report, confusion, training_log]):
        st.warning("⚠️ No se encontraron archivos de métricas en `models/model_metrics/`")
        st.info("Asegúrate de que los archivos generados durante el entrenamiento estén en la carpeta correcta.")
    else:
        # ===== SECCIÓN 1: MÉTRICAS GLOBALES =====
        if report:
            st.subheader("🎯 Métricas por Clase")
            
            # Convertir reporte a DataFrame para mejor visualización
            report_df = pd.DataFrame(report).transpose()
            
            # Filtrar solo las clases (excluir accuracy, macro avg, weighted avg)
            classes = [c for c in report_df.index if c not in ['accuracy', 'macro avg', 'weighted avg']]
            report_classes = report_df.loc[classes]
            
            # Mostrar métricas en columnas
            cols = st.columns(4)
            metricas = ['precision', 'recall', 'f1-score']
            colores_metricas = {"precision": "blue", "recall": "green", "f1-score": "orange"}
            
            for idx, clase in enumerate(classes):
                with st.expander(f"📌 {clase.replace('_', ' ').title()}"):
                    for metrica in metricas:
                        valor = report_classes.loc[clase, metrica]
                        st.metric(
                            label=metrica.upper(),
                            value=f"{valor:.3f}",
                            delta=None
                        )
            
            # Mostrar accuracy global
            if 'accuracy' in report_df.index:
                acc = report_df.loc['accuracy', 'precision'] if 'precision' in report_df.columns else report_df.loc['accuracy']
                st.success(f"### 🎯 Accuracy Global: **{acc:.2%}**")
        
        # ===== SECCIÓN 2: MATRIZ DE CONFUSIÓN =====
        if confusion is not None:
            st.subheader("🔢 Matriz de Confusión")
            
            # Dar formato a los nombres de las clases
            confusion.columns = [col.replace('_', ' ').title() for col in confusion.columns]
            confusion.index = [idx.replace('_', ' ').title() for idx in confusion.index]
            
            # Mostrar como DataFrame con estilo
            st.dataframe(
                confusion,
                use_container_width=True,
                column_config={
                    col: st.column_config.NumberColumn(col, format="%d")
                    for col in confusion.columns
                }
            )
            
            # Mostrar heatmap textual
            st.caption("📖 **Interpretación**: Filas = Valores Reales, Columnas = Predicciones")
        
        # ===== SECCIÓN 3: HISTORIAL DE ENTRENAMIENTO =====
        # ===== SECCIÓN 3: HISTORIAL DE ENTRENAMIENTO =====
        if history:
            st.subheader("📉 Evolución del Entrenamiento")
            
            # Convertir a DataFrame (ya es un dict, no necesita conversión)
            history  = history.pop("lr")
            history_df = pd.DataFrame(history)
            
            # Debug: mostrar las columnas disponibles (comenta después de verificar)
            # st.write("**Columnas disponibles:**", list(history_df.columns))
            
            # Verificar qué columnas existen realmente
            columnas_disponibles = history_df.columns.tolist()
            
            # Gráfico de pérdida (loss)
            col_loss, col_acc = st.columns(2)
            
            with col_loss:
                st.markdown("**Pérdida (Loss)**")
                # Buscar columnas de loss
                loss_cols = [col for col in columnas_disponibles if 'loss' in col.lower()]
                if loss_cols:
                    st.line_chart(
                        history_df[loss_cols],
                        y_label="Loss"
                    )
                else:
                    st.warning("No se encontraron datos de 'loss'")
            
            with col_acc:
                st.markdown("**Precisión (Accuracy)**")
                # Buscar columnas de accuracy
                acc_cols = [col for col in columnas_disponibles if 'acc' in col.lower()]
                if acc_cols:
                    st.line_chart(
                        history_df[acc_cols],
                        y_label="Accuracy"
                    )
                else:
                    st.warning("No se encontraron datos de 'accuracy'")
            
            # Mostrar learning rate si existe
            if 'lr' in columnas_disponibles:
                st.markdown("**Tasa de Aprendizaje (Learning Rate)**")
                st.line_chart(history_df['lr'], y_label="LR")
            elif 'learning_rate' in columnas_disponibles:
                st.markdown("**Tasa de Aprendizaje (Learning Rate)**")
                st.line_chart(history_df['learning_rate'], y_label="LR")
        
        # ===== SECCIÓN 4: LOG DE ENTRENAMIENTO =====
        if training_log is not None and not training_log.empty:
            with st.expander("📋 Ver Log Detallado de Entrenamiento"):
                st.dataframe(training_log, use_container_width=True)
        
        # ===== SECCIÓN 5: RESUMEN ESTADÍSTICO =====
        st.subheader("📊 Resumen Estadístico")
        
        col_res1, col_res2, col_res3 = st.columns(3)
        
        if history:
            with col_res1:
                mejor_acc = max(history.get('val_accuracy', [0]))
                st.metric("Mejor Accuracy Validación", f"{mejor_acc:.2%}")
            
            with col_res2:
                mejor_loss = min(history.get('val_loss', [float('inf')]))
                st.metric("Mejor Loss Validación", f"{mejor_loss:.4f}")
            
            with col_res3:
                epocas = len(history.get('loss', []))
                st.metric("Total de Épocas", epocas)
        
        # Información de los archivos cargados
        with st.expander("ℹ️ Archivos de métricas cargados"):
            metrics_dir = Path("models/model_metrics")
            if metrics_dir.exists():
                for file in metrics_dir.iterdir():
                    size = file.stat().st_size
                    if size < 1024:
                        size_str = f"{size} B"
                    elif size < 1024 * 1024:
                        size_str = f"{size / 1024:.1f} KB"
                    else:
                        size_str = f"{size / (1024 * 1024):.1f} MB"
                    st.write(f"- `{file.name}` ({size_str})")
