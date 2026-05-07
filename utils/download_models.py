import os
import gdown
from pathlib import Path
import streamlit as st

def download_model(progress_bar=None):
    """Descarga el modelo con barra de progreso opcional"""
    
    MODEL_DIR = Path(__file__).parent.parent / "models"
    MODEL_PATH = MODEL_DIR / "dog_emotion_classifier.h5"
    URL = "https://drive.google.com/file/d/1ceGVgTTLos_b586g0HsdH6VQMuVQkEfo/view?usp=sharing"
    
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    
    if MODEL_PATH.exists():
        return MODEL_PATH
    
    # Si estamos en Streamlit, mostrar barra de progreso
    if progress_bar is not None:
        progress_bar.progress(10, text="📥 Conectando con Google Drive...")
    
    
    # Callback para actualizar progreso
    def update_progress(current, total, width=50):
        if progress_bar is not None and total > 0:
            percent = current / total
            progress_bar.progress(percent, text=f"⬇️ Descargando: {current/1024/1024:.1f}/{total/1024/1024:.1f} MB")
    
    try:
        gdown.download(
            URL, 
            str(MODEL_PATH), 
            quiet=False,
            fuzzy=True  # Permite URLs más flexibles
        )
        return MODEL_PATH
    except Exception as e:
        # Fallback: intentar con URL directa de descarga
        raise FileNotFoundError("No se encontró el modelo")
