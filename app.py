import streamlit as st

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
