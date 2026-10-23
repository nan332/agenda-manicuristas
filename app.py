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
    margin: 20px 0;
}
.luxury-card {
    background: #14161c;
    border: 1px solid #282b35;
    border-radius: 14px;
    padding: 16px;
}
.card-title {
    font-size: 14px;
    font-weight: 700;
    color: #e5c158;
    margin-bottom: 5px;
}
.card-desc {
    font-size: 12px;
    color: #9da3af;
    line-height: 1.4;
}

/* Contenedor de la demo interactiva */
.mockup-app {
    background: #12141a;
    border: 1px solid #333845;
    border-radius: 18px;
    padding: 22px;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
    margin: 20px 0;
}

/* Ticket de resumen */
.ticket-box {
    background: #191c24;
    border-left: 4px solid #d4af37;
    border-radius: 10px;
    padding: 14px;
    margin: 15px 0;
}

/* Botón interactivo de la demo */
.btn-gold {
    display: block;
    background: linear-gradient(135deg, #d4af37 0%, #aa820a 100%);
    color: #0b0c0e !important;
    text-align: center;
    padding: 15px;
    font-size: 16px;
    font-weight: 800;
    border-radius: 10px;
    text-decoration: none;
    box-shadow: 0 4px 15px rgba(212, 175, 55, 0.25);
    margin-top: 10px;
}

/* Botón de compra WhatsApp */
.btn-whatsapp {
    display: block;
    background: linear-gradient(135deg, #25D366 0%, #1da851 100%);
    color: white !important;
    text-align: center;
    padding: 18px 20px;
    font-size: 18px;
    font-weight: 800;
    border-radius: 12px;
    text-decoration: none;
    box-shadow: 0 6px 20px rgba(37, 211, 102, 0.35);
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)

# 3. LOGO EN PANTALLA
try:
    st.image("logo.png", width=220)
except Exception:
    st.markdown("<h2 style='text-align:center; color:#d4af37;'>NAN • AGENDAS AUTOMÁTICAS</h2>", unsafe_allow_html=True)

# 4. ENCABEZADO
st.markdown('<div style="text-align:center;"><span class="gold-badge">SISTEMAS EXCLUSIVOS PARA NAIL ARTISTS</span></div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">Deja de perder 2 horas al día contestando precios en WhatsApp</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Tu propio link profesional para tu perfil de Instagram. Tus clientas eligen servicio, día y hora solas, y te mandan su anticipo sin interrumpir tus aplicaciones.</div>', unsafe_allow_html=True)

# 5. BENEFICIOS
st.markdown("""
<div class="grid-cards">
    <div class="luxury-card">
        <div class="card-title">💅 Cero interrupciones</div>
        <div class="card-desc">No detengas la aplicación de acrílico para cotizar el mismo servicio una y otra vez.</div>
    </div>
    <div class="luxury-card">
        <div class="card-title">💳 Con anticipo listo</div>
        <div class="card-desc">El mensaje llega pidiéndote tu tarjeta para transferir antes de apartar la cita.</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# 6. DEMO INTERACTIVA
st.markdown("### 📱 Pruébalo tú misma")
st.caption("Prueba cómo agendaría una clienta en tu futuro enlace:")

st.markdown('<div class="mockup-app">', unsafe_allow_html=True)

servicios = {
    "Acrílico Esculpido (Punta Coffin / Almendra)": 480,
    "Baño de Acrílico + Gel Semi": 350,
    "Gelish con Diseño Mano Alzada": 280,
    "Retiro de Acrílico + Manicura Rusa": 220
}

servicio_elegido = st.selectbox("1. Selecciona el servicio deseado:", list(servicios.keys()))
precio = servicios[servicio_elegido]

col1, col2 = st.columns(2)
with col1:
    fecha = st.date_input("2. Día preferido:", min_value=date.today())
with col2:
    horario = st.selectbox("3. Horario disponible:", ["11:00 AM", "1:30 PM", "4:00 PM", "6:30 PM"])

nombre = st.text_input("4. Nombre de la clienta:", "Sofia Montes")

# Recuadro resumen
st.markdown(f"""
<div class="ticket-box">
    <div style="font-size: 12px; color: #d4af37; font-weight: 700; letter-spacing: 0.5px;">RESUMEN DE RESERVA</div>
    <div style="font-size: 15px; font-weight: 600; margin-top: 3px; color: #fff;">{servicio_elegido}</div>
    <div style="font-size: 13px; color: #9da3af;">Fecha: {fecha.strftime('%d/%m/%Y')} • {horario}</div>
    <div style="font-size: 16px; font-weight: 800; color: #25D366; margin-top: 5px;">Total estimado: ${precio} MXN</div>
</div>
""", unsafe_allow_html=True)

# Generación del mensaje de prueba
mensaje_wa = (
    f"¡Hola! Quiero agendar una cita ✨\n\n"
    f"👤 Clienta: {nombre}\n"
    f"💅 Servicio: {servicio_elegido} (${precio} MXN)\n"
    f"📅 Fecha: {fecha.strftime('%d/%m/%Y')} a las {horario}\n\n"
    f"¿Me pasas tus datos bancarios para transferirte el anticipo y confirmar mi espacio?"
)
link_demo_wa = f"https://wa.me/525539233647?text={urllib.parse.quote(mensaje_wa)}"

st.markdown(f'''
<a class="btn-gold" href="{link_demo_wa}" target="_blank">
    ✨ Probar cómo llega la cita a tu WhatsApp →
</a>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# 7. CIERRE DE VENTA
st.markdown("### 👑 Pide tu sistema personalizado")
st.markdown("""
* ✅ **Tus servicios y lista de precios oficial.**
* ✅ **Tus horarios y días de atención configurados.**
* ✅ **Tu propio botón conectado directo a tu número de WhatsApp.**
* ✅ **Listo para colocar en la biografía de tu Instagram o TikTok.**
* ⚡ **Entrega garantizada en menos de 24 horas.**
""")

st.markdown("#### Precio especial de lanzamiento: **$499 MXN** *(Pago único • Sin mensualidades)*")

WHATSAPP = "525539233647"
msg_compra = "Hola Nancy, vi tu página de NAN Agendas Automáticas. Quiero mi enlace para manicuristas por $499 MXN."
link_compra = f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(msg_compra)}"

st.markdown(f'''
<a class="btn-whatsapp" href="{link_compra}" target="_blank">
    💬 QUIERO MI AGENDA POR $499 MXN →
</a>
''', unsafe_allow_html=True)

st.caption("NAN Agendas Automáticas • Nancy Rufino • CDMX")
