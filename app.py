import streamlit as st
import urllib.parse
from datetime import date

# 1. Configuración de página
st.set_page_config(
    page_title="NAN Agendas Automáticas | Para Nail Artists",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Tu número de WhatsApp de ventas (Donde te compran el sistema)
WHATSAPP_VENTAS = "5215500000000"  # Pon aquí tu número con lada internacional

# 3. CSS Profesional - Estilo Landing Page Dark & Gold
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    #MainMenu, footer, header {visibility: hidden !important;}
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 4rem !important;
        max-width: 650px;
    }

    .stApp {
        background: radial-gradient(circle at 50% 0%, #1e1b18 0%, #0d0c0b 100%);
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #f5f5f4;
    }

    /* Logo Circular con Efecto Glow Dorado (Adiós al cuadro blanco plano) */
    .logo-hero {
        text-align: center;
        padding: 10px 0 15px 0;
    }

    .logo-glow-wrapper {
        display: inline-block;
        padding: 5px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(212,175,55,0.4) 0%, rgba(0,0,0,0) 70%);
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.25);
    }

    .logo-img {
        width: 140px;
        height: 140px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid rgba(212, 175, 55, 0.8);
        background: #000;
    }

    /* Badge superior */
    .badge-pill {
        display: inline-block;
        background: rgba(212, 175, 55, 0.1);
        border: 1px solid rgba(212, 175, 55, 0.5);
        color: #fde047;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 2px;
        padding: 6px 18px;
        border-radius: 50px;
        text-transform: uppercase;
        margin-top: 10px;
    }

    /* Título principal con impacto */
    .main-headline {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-weight: 800;
        font-size: 30px;
        line-height: 1.25;
        text-align: center;
        margin-top: 15px;
        margin-bottom: 15px;
        color: #ffffff;
    }

    .highlight-gold {
        background: linear-gradient(135deg, #fef08a 0%, #d4af37 50%, #aa771c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .sub-headline {
        text-align: center;
        color: #a8a29e;
        font-size: 15px;
        line-height: 1.6;
        margin-bottom: 25px;
        padding: 0 10px;
    }

    /* Beneficios en cajas elegantes */
    .benefit-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 14px;
        margin-bottom: 25px;
    }

    .benefit-card {
        background: #151413;
        border: 1px solid rgba(212, 175, 55, 0.25);
        border-radius: 14px;
        padding: 18px 14px;
        transition: all 0.3s ease;
    }

    .benefit-icon {
        font-size: 24px;
        margin-bottom: 8px;
    }

    .benefit-title {
        color: #fde047;
        font-weight: 700;
        font-size: 14px;
        margin-bottom: 6px;
    }

    .benefit-desc {
        color: #9ca3af;
        font-size: 12px;
        line-height: 1.4;
    }

    /* Marco de Demo */
    .demo-frame {
        background: #11100f;
        border: 1px dashed rgba(212, 175, 55, 0.4);
        border-radius: 16px;
        padding: 20px;
        margin-top: 25px;
        margin-bottom: 25px;
    }

    .demo-tag {
        font-family: 'Cinzel', serif;
        font-size: 13px;
        color: #d4af37;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-align: center;
        margin-bottom: 15px;
        text-transform: uppercase;
    }

    /* Botón CTA Dorado de Venta */
    .cta-btn {
        display: block;
        width: 100%;
        text-align: center;
        background: linear-gradient(135deg, #f59e0b 0%, #b45309 100%);
        color: #0c0a09 !important;
        font-weight: 800;
        font-size: 16px;
        letter-spacing: 1px;
        text-transform: uppercase;
        padding: 18px 15px;
        border-radius: 12px;
        text-decoration: none;
        margin: 20px 0 10px 0;
        box-shadow: 0 4px 25px rgba(217, 119, 6, 0.45);
        transition: all 0.3s ease;
    }

    .cta-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 30px rgba(245, 158, 11, 0.65);
    }

    .guarantee-text {
        text-align: center;
        font-size: 12px;
        color: #78716c;
        margin-top: 10px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 4. Cabecera con tu Logo 'NAN' y Propuesta de Valor
# Puedes colocar aquí el archivo local "logo.png" si lo subes a tu GitHub junto al app.py
LOGO_PATH = "https://images.unsplash.com/photo-1604654894610-df63bc536371?w=400&auto=format&fit=crop&q=80" 

st.markdown(f"""
<div class="logo-hero">
    <div class="logo-glow-wrapper">
        <img src="{LOGO_PATH}" class="logo-img" alt="NAN Agendas">
    </div>
    <br>
    <span class="badge-pill">Sistemas Exclusivos para Nail Artists</span>
</div>

<h1 class="main-headline">
    Deja de perder 2 horas al día contestando precios en <span class="highlight-gold">WhatsApp</span>
</h1>

<p class="sub-headline">
    Tu propio <b>link personalizado para biografía de Instagram o TikTok</b>. Tus clientas seleccionan servicio, fecha y hora solas, y te mandan su comprobante de anticipo sin que tengas que interrumpir tus aplicaciones de uñas.
</p>
""", unsafe_allow_html=True)

# 5. Tarjetas de Beneficios (Por qué te lo van a comprar)
st.markdown("""
<div class="benefit-grid">
    <div class="benefit-card">
        <div class="benefit-icon">💅</div>
        <div class="benefit-title">Cero Interrupciones</div>
        <div class="benefit-desc">No pares la aplicación de acrílico ni quites los guantes para responder: <i>"¿Cuánto cuesta el set?"</i>.</div>
    </div>
    <div class="benefit-card">
        <div class="benefit-icon">💳</div>
        <div class="benefit-title">Con Anticipo Listo</div>
        <div class="benefit-desc">El mensaje les exige su anticipo bancario antes de asegurar el lugar en tu mesa.</div>
    </div>
    <div class="benefit-card">
        <div class="benefit-icon">📱</div>
        <div class="benefit-title">Link en tu Bio</div>
        <div class="benefit-desc">Ponlo en tu Instagram, TikTok o Facebook y vende 24/7 en automático.</div>
    </div>
    <div class="benefit-card">
        <div class="benefit-icon">👑</div>
        <div class="benefit-title">Estatus Profesional</div>
        <div class="benefit-desc">Da una imagen de estudio de alta gama, cobra lo justo y filtra a clientas dudosas.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 6. DEMO INTERACTIVA (Para que la manicurista vea lo que le vas a entregar)
st.markdown("""
<div class="demo-frame">
    <div class="demo-tag">✨ Pruébalo aquí: Así de fácil agendarán tus clientas ✨</div>
""", unsafe_allow_html=True)

col_demo1, col_demo2 = st.columns(2)
with col_demo1:
    demo_servicio = st.selectbox(
        "Servicio a elegir:",
        ["Acrílico Escultural", "Soft Gel + Cristales", "Mano Alzada / 3D", "Manicura Rusa"]
    )
with col_demo2:
    demo_hora = st.selectbox("Horario preferido:", ["11:00 AM", "01:30 PM", "04:00 PM", "06:30 PM"])

st.caption("⚡ Al dar clic en 'Agendar', tu clienta te enviará un WhatsApp con todo detallado y solicitando tus datos de transferencia.")
st.markdown("</div>", unsafe_allow_html=True)

# 7. Llamado a la Acción (CTA) de Compra a tu WhatsApp
mensaje_interes = urllib.parse.quote(
    "¡Hola NAN Agendas! 👋 Vi su sistema automático para Nail Artists y quiero adquirir mi link personalizado con mi propio logo, catálogo y precios para mi estudio."
)
enlace_compra = f"https://wa.me/{WHATSAPP_VENTAS}?text={mensaje_interes}"

st.markdown(f"""
<a href="{enlace_compra}" target="_blank" class="cta-btn">
    👉 QUIERO MI SISTEMA DE AGENDAS AHORA
</a>
<div class="guarantee-text">
    🔒 Entrega en 24 horas • Configuración 100% personalizada con tu logo y catálogo • Pago único.
</div>
""", unsafe_allow_html=True)
