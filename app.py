import streamlit as st
import urllib.parse
from datetime import date

st.set_page_config(
    page_title="NAN Studio | Agenda Digital para Manicuristas",
    page_icon="✨",
    layout="centered"
)

# ESTILOS CSS PROFESIONALES DE ALTA CONVERSIÓN
st.markdown("""
<style>
/* Ocultar marcas de agua y menús de Streamlit */
#MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stHeader"], [data-testid="stDecoration"], .stDeployButton, div[class*="viewerBadge"] {
    display: none !important;
    visibility: hidden !important;
}

/* Tipografía base y fondo */
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
.stApp {
    background-color: #0b0d11;
    color: #e6edf3;
}

/* Banner de categoría */
.pill-badge {
    display: inline-block;
    background: rgba(255, 117, 168, 0.15);
    color: #ff75a8;
    border: 1px solid rgba(255, 117, 168, 0.35);
    padding: 6px 14px;
    border-radius: 50px;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
}

/* Título principal con degradado */
.main-title {
    font-size: 32px;
    font-weight: 800;
    line-height: 1.25;
    background: linear-gradient(90deg, #ffffff 30%, #ff9ebb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 16px;
    color: #8b949e;
    line-height: 1.5;
    margin-bottom: 25px;
}

/* Tarjetas de beneficios */
.grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 20px 0;
}
.benefit-card {
    background: #141820;
    border: 1px solid #232936;
    border-radius: 12px;
    padding: 14px;
}
.benefit-title {
    font-size: 14px;
    font-weight: 700;
    color: #f0f6fc;
    margin-bottom: 4px;
}
.benefit-desc {
    font-size: 12px;
    color: #8b949e;
    line-height: 1.4;
}

/* Marco de la App Demo */
.mockup-container {
    background: #131722;
    border: 1px solid #2d3446;
    border-radius: 18px;
    padding: 22px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    margin: 20px 0;
}

/* Ticket de confirmación */
.ticket {
    background: #1c2230;
    border-left: 4px solid #ff75a8;
    border-radius: 8px;
    padding: 14px;
    margin: 15px 0;
}

/* Botón llamativo WhatsApp */
.wa-button {
    display: block;
    background: linear-gradient(135deg, #25D366 0%, #1ebe5d 100%);
    color: white !important;
    text-align: center;
    padding: 18px 24px;
    font-size: 18px;
    font-weight: 800;
    border-radius: 12px;
    text-decoration: none;
    box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)

# ENCABEZADO
st.markdown('<span class="pill-badge">✨ SISTEMA DE CITAS PARA NAIL ARTISTS</span>', unsafe_allow_html=True)
st.markdown('<div class="main-title">Deja de perder clientas y horas cotizando por mensaje</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Un enlace elegante para tu perfil de Instagram que muestra tus trabajos, filtra tus precios y te manda citas listas con anticipo a tu WhatsApp.</div>', unsafe_allow_html=True)

# CARDS DE VALOR
st.markdown("""
<div class="grid-container">
    <div class="benefit-card">
        <div class="benefit-title">💅 Cero interrupciones</div>
        <div class="benefit-desc">No sueltes tu pincel ni la lámpara para contestar preguntas de precios.</div>
    </div>
    <div class="benefit-card">
        <div class="benefit-title">💵 Con anticipo listo</div>
        <div class="benefit-desc">El mensaje llega redactado directo a pedir tu tarjeta para transferir.</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# DEMO INTERACTIVA
st.markdown("### 📱 Pruébalo tú misma")
st.caption("Así verán tus clientas tu enlace personalizado:")

st.markdown('<div class="mockup-container">', unsafe_allow_html=True)

servicios = {
    "Acrílico Esculpido (Punta Coffin / Almond)": 480,
    "Baño de Acrílico + Gel Semi": 350,
    "Gelish con Diseño Mano Alzada": 280,
    "Retiro de Acrílico + Manicura Rusa": 220
}

servicio_elegido = st.selectbox(
    "1. Selecciona el servicio deseado:",
    list(servicios.keys())
)
precio = servicios[servicio_elegido]

col1, col2 = st.columns(2)
with col1:
    fecha = st.date_input("2. Día preferido:", min_value=date.today())
with col2:
    horario = st.selectbox("3. Horario:", ["11:00 AM", "1:30 PM", "4:00 PM", "6:30 PM"])

nombre = st.text_input("4. Nombre de la clienta:", "Sofia Montes")

# Ficha visual estilo Ticket
st.markdown(f"""
<div class="ticket">
    <div style="font-size: 13px; color: #ff75a8; font-weight: 700;">RESUMEN DE RESERVA</div>
    <div style="font-size: 15px; font-weight: 600; margin-top: 4px;">{servicio_elegido}</div>
    <div style="font-size: 13px; color: #8b949e;">Fecha: {fecha.strftime('%d/%m/%Y')} • {horario}</div>
    <div style="font-size: 16px; font-weight: 800; color: #25D366; margin-top: 6px;">Total aproximado: ${precio} MXN</div>
</div>
""", unsafe_allow_html=True)

# Generación del link de WhatsApp
mensaje_wa = (
    f"¡Hola! Quiero agendar una cita ✨\n\n"
    f"👤 Clienta: {nombre}\n"
    f"💅 Servicio: {servicio_elegido} (${precio} MXN)\n"
    f"📅 Fecha: {fecha.strftime('%d/%m/%Y')} a las {horario}\n\n"
    f"¿Me pasas tus datos bancarios para depositar el anticipo y asegurar mi espacio?"
)
link_demo_wa = f"https://wa.me/525539233647?text={urllib.parse.quote(mensaje_wa)}"

st.markdown(f'''
<a href="{link_demo_wa}" target="_blank" style="display:block; background:#ff75a8; color:white; padding:15px; text-align:center; font-size:15px; font-weight:bold; border-radius:10px; text-decoration:none; margin-top:10px;">
    👉 Probar cómo llega la cita a WhatsApp
</a>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# OFERTA Y LLAMADO A LA ACCIÓN
st.markdown("### 🚀 Obtén tu enlace personalizado")
st.markdown("""
* ✅ **Tus servicios y lista de precios oficial.**
* ✅ **Tus horarios y días disponibles configurados.**
* ✅ **Tu propio botón conectado directo a tu WhatsApp.**
* ✅ **Lista para poner en tu biografía de Instagram o TikTok.**
* ⚡ **Entrega en menos de 24 horas.**
""")

st.markdown("#### Inversión: **$499 MXN** *(Pago único • Sin mensualidades)*")

WHATSAPP = "525539233647"
msg_compra = "Hola Nancy, quiero mi agenda digital para manicuristas por $499. ¿Cómo le hacemos?"
link_compra = f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(msg_compra)}"

st.markdown(f'''
<a class="wa-button" href="{link_compra}" target="_blank">
    💬 QUIERO MI AGENDA POR $499 MXN
</a>
''', unsafe_allow_html=True)

st.caption("NAN Studio Tech • Creadora de sistemas de citas para Manicuristas • CDMX")
