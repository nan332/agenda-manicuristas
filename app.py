import streamlit as st
from datetime import date, time
import urllib.parse

# 1. Configuración de página
st.set_page_config(
    page_title="Agenda VIP | Beauty & Nails",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Estilos personalizados Premium (Negro Profundo + Oro Metálico)
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Montserrat:wght@300;400;500;600&display=swap');

    /* Ocultar marcas y menús de Streamlit */
    #MainMenu, footer, header {visibility: hidden !important;}
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 620px;
    }

    /* Fondo principal */
    .stApp {
        background: radial-gradient(circle at top, #1c1917 0%, #0c0a09 100%);
        font-family: 'Montserrat', sans-serif;
        color: #f5f5f4;
    }

    /* Contenedor del encabezado */
    .hero-container {
        text-align: center;
        padding: 24px 20px 10px 20px;
        margin-bottom: 25px;
    }

    .brand-logo-ring {
        width: 105px;
        height: 105px;
        margin: 0 auto 16px auto;
        border-radius: 50%;
        padding: 3px;
        background: linear-gradient(135deg, #f59e0b, #d97706, #78350f, #fbbf24);
        box-shadow: 0 0 25px rgba(245, 158, 11, 0.35);
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .brand-logo-img {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        object-fit: cover;
        background-color: #121212;
    }

    .brand-title {
        font-family: 'Cinzel', serif;
        font-size: 28px;
        font-weight: 700;
        background: linear-gradient(90deg, #fef08a, #d97706, #fde047);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 2px;
        margin-bottom: 6px;
        text-transform: uppercase;
    }

    .brand-subtitle {
        color: #a8a29e;
        font-size: 13px;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    .badge-gold {
        display: inline-block;
        background: rgba(217, 119, 6, 0.15);
        border: 1px solid rgba(245, 158, 11, 0.4);
        color: #fde047;
        font-size: 11px;
        padding: 4px 14px;
        border-radius: 20px;
        letter-spacing: 1px;
    }

    /* Tarjetas oscuras con borde dorado */
    .booking-card {
        background: #171717;
        border: 1px solid rgba(217, 119, 6, 0.3);
        border-radius: 18px;
        padding: 22px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }

    /* Inputs estilizados */
    label {
        color: #e7e5e4 !important;
        font-weight: 500 !important;
        font-size: 13px !important;
        letter-spacing: 0.5px;
    }

    .stTextInput>div>div>input, 
    .stSelectbox>div>div, 
    .stDateInput>div>div>input {
        background-color: #262626 !important;
        color: #f5f5f4 !important;
        border: 1px solid #44403c !important;
        border-radius: 10px !important;
    }

    /* Botón VIP de WhatsApp */
    .btn-whatsapp {
        display: block;
        width: 100%;
        text-align: center;
        background: linear-gradient(135deg, #f59e0b 0%, #b45309 100%);
        color: #0c0a09 !important;
        font-weight: 700;
        font-size: 16px;
        letter-spacing: 1px;
        text-transform: uppercase;
        padding: 16px 20px;
        border-radius: 12px;
        text-decoration: none;
        margin-top: 20px;
        box-shadow: 0 4px 20px rgba(217, 119, 6, 0.4);
        transition: all 0.3s ease;
    }

    .btn-whatsapp:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(245, 158, 11, 0.6);
        color: #000 !important;
    }

    .note-anticipo {
        text-align: center;
        color: #78716c;
        font-size: 11px;
        margin-top: 14px;
        line-height: 1.5;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. Datos del Negocio (Personaliza aquí)
WHATSAPP_NUMERO = "5215500000000"  # Reemplaza con tu número a 10 dígitos con código de país
LOGO_URL = "https://images.unsplash.com/photo-1604654894610-df63bc536371?w=400&auto=format&fit=crop&q=80"

# 4. Encabezado con Logo y Branding
st.markdown(f"""
<div class="hero-container">
    <div class="brand-logo-ring">
        <img src="{LOGO_URL}" class="brand-logo-img" alt="Logo">
    </div>
    <div class="brand-title">Atelier Nails & Spa</div>
    <div class="brand-subtitle">Diseño Exclusivo • Cuidado de Autor</div>
    <span class="badge-gold">AGENDA EN LÍNEA • ATENCIÓN VIP</span>
</div>
""", unsafe_allow_html=True)

# 5. Formulario interactivo
with st.container():
    st.markdown('<div class="booking-card">', unsafe_allow_html=True)
    
    nombre_cliente = st.text_input("✨ Tu nombre completo:", placeholder="Ej. Sofia Ramos")
    
    servicio_seleccionado = st.selectbox(
        "💅 Servicio que deseas agendar:",
        [
            "Acrílico Escultural (Diseño VIP) - $650 MXN",
            "Soft Gel Express + Efecto Espejo/Glitter - $450 MXN",
            "Mani Ruso + Nivelación Rubber - $400 MXN",
            "Retoque / Mantenimiento Acrílico - $350 MXN",
            "Pedicure Spa Profundo + Esmaltado - $500 MXN",
            "Retiro de Sistema + Tratamiento Nutritivo - $200 MXN"
        ]
    )
    
    col1, col2 = st.columns(2)
    with col1:
        fecha_cita = st.date_input("📅 Fecha:", min_value=date.today())
    with col2:
        hora_cita = st.selectbox(
            "⏰ Horario:",
            ["10:00 AM", "12:00 PM", "02:30 PM", "04:30 PM", "06:30 PM"]
        )
        
    comentarios = st.text_input("💎 ¿Deseas algún diseño o detalle especial?", placeholder="Ej. Cristales Swarovski, mano alzada, french...")

    st.markdown('</div>', unsafe_allow_html=True)

# 6. Generación del Mensaje para WhatsApp
if nombre_cliente.strip():
    mensaje = (
        f"👑 *SOLICITUD DE CITA VIP*\n\n"
        f"• *Cliente:* {nombre_cliente}\n"
        f"• *Servicio:* {servicio_seleccionado}\n"
        f"• *Fecha:* {fecha_cita.strftime('%d/%m/%Y')}\n"
        f"• *Horario:* {hora_cita}\n"
        f"• *Detalles:* {comentarios if comentarios.strip() else 'Diseño estándar'}\n\n"
        f"✨ _Hola, quedo atenta para realizar el anticipo y asegurar mi horario. ¡Muchas gracias!_"
    )
    
    url_whatsapp = f"https://wa.me/{WHATSAPP_NUMERO}?text={urllib.parse.quote(mensaje)}"
    
    st.markdown(
        f'<a href="{url_whatsapp}" target="_blank" class="btn-whatsapp">📲 Agendar y Confirmar por WhatsApp</a>',
        unsafe_allow_html=True
    )
else:
    st.info("Ingresa tu nombre arriba para habilitar el enlace directo de confirmación.")

st.markdown(
    '<div class="note-anticipo">🔒 Tu cita queda formalmente reservada tras validar tu comprobante de anticipo. Atención personalizada bajo reserva previa.</div>',
    unsafe_allow_html=True
)
