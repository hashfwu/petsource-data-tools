import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from utils.download_models import download_model

st.set_page_config(page_title="PetSource Data Tools", page_icon="🐾", layout="wide")

with st.sidebar:
    st.image("https://via.placeholder.com/150x80?text=PetSource", width=True)
    st.markdown("# PetSource Data Tools")
    st.markdown("---")
    
    st.page_link("app.py", label="Inicio", icon="🏠")
    st.page_link("pages/page_01.py", label="Análisis", icon="📊")
    st.page_link("pages/page_02.py", label="Historial", icon="📋")
    st.page_link("pages/page_03.py", label="Analizador de Emociones", icon="😊")

st.title("PetSource Data Tools")
st.markdown("Bienvenido a la plataforma de análisis emocional para mascotas.")

col1, col2 = st.columns(2)

with col1:
    st.info("📊 **Análisis de datos** - ¿Cúal es el producto que más se vende?")
with col2:
    st.success("😊 **Analizador de emociones** - Sube una foto o usa la cámara")

@st.cache_resource
def load_model_with_auto_download():
    """Carga el modelo, descargándolo primero si es necesario"""
    
    with st.spinner("🔍 Verificando modelo..."):
        # Descargar modelo si no existe
        model_path = download_model()
        
        # Mostrar progreso
        st.info(f"📦 Modelo encontrado en: {model_path}")
    
    # Cargar el modelo
    with st.spinner("🧠 Cargando modelo en memoria..."):
        import tensorflow as tf
        model = tf.keras.models.load_model(model_path)
    
    return model

# Cargar modelo (solo una vez gracias a cache)
try:
    model = load_model_with_auto_download()
    st.success("✅ Modelo listo para usar")
    model_ready = True
except Exception as e:
    st.error(f"❌ Error cargando modelo: {e}")
    model_ready = False
