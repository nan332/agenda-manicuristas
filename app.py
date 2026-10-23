import streamlit as st
import urllib.parse
from datetime import date

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="NAN | Agendas Automáticas para Manicuristas",
    page_icon="💅",
    layout="centered"
)

# 2. ESTILOS VISUALES (NEGRO Y DORADO, SIN BARRAS FLOTANTES)
st.markdown("""
<style>
/* Ocultar elementos nativos de Streamlit */
#MainMenu, header, footer, 
[data-testid="stToolbar"], 
[data-testid="stHeader"], 
[data-testid="stDecoration"], 
.stDeployButton, 
div[class*="viewerBadge"],
div[data-testid="stStatusWidget"],
div[data-testid="stBottom"],
div[class*="bottomBar"],
footer[data-testid="stFooter"] {
    display: none !important;
    visibility: hidden !important;
}

div[style*="position: fixed"][style*="bottom:"],
div[style*="position: fixed"][style*="right:"] {
    display: none !important;
    visibility: hidden !important;
}

/* Fondo principal */
.stApp {
    background-color: #0b0c0e;
    color: #f5f5f7;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

/* Centrar imagen de logo */
[data-testid="stImage"] {
    display: flex;
    justify-content: center;
    margin-bottom: 5px;
}

/* Títulos y acentos dorados */
.gold-badge {
    display: inline-block;
    background: rgba(212, 175, 55, 0.12);
    color: #e5c158;
    border: 1px solid rgba(212, 175, 55, 0.4);
    padding: 6px 16px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.6px;
    margin-bottom: 12px;
}

.hero-title {
    font-size: 30px;
    font-weight: 800;
    line-height: 1.25;
    background: linear-gradient(135deg, #ffffff 40%, #d4af37 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 12px;
    text-align: center;
}

.hero-subtitle {
    font-size: 15px;
    color: #a0a6b2;
    line-height: 1.5;
    text-align: center;
    margin-bottom: 25px;
}

/* Tarjetas de beneficios */
.grid-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin
