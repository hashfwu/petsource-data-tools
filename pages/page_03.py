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

tab1, tab2 = st.tabs(["📸 Tomar foto", "📁 Subir imagen"])
image = None

with tab1:
    img = st.camera_input("Toma una foto de tu mascota")
    if img:
        image = Image.open(img)

with tab2:
    img = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])
    if img:
        image = Image.open(img)

if image and model_ready:
    with st.spinner("Analizando..."):
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
            
            for emo, prob in zip(emociones, predictions):
                st.progress(float(prob), text=f"{emo}: {prob:.1%}")
