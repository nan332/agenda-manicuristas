import streamlit as st
import urllib.parse
from datetime import date, time

st.set_page_config(
    page_title="NAN - Agendas Automáticas para Manicuristas",
    page_icon="💅",
    layout="centered"
)

# Estilos limpios y eliminación de elementos de Streamlit
st.markdown("""
<style>
#MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stHeader"], [data-testid="stDecoration"], .stDeployButton, div[class*="viewerBadge"] {
    display: none !important;
    visibility: hidden !important;
}
.stApp {
    background-color: #0d0f12;
    color: #f1f1f1;
}
.demo-box {
    background: #161a22;
    border: 1px solid #30363d;
    border-radius: 14px;
    padding: 20px;
    margin-top: 10px;
}
.badge {
    background-color: #ff4b8b;
    color: white;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Intento de cargar logo si existe, o banner de texto
try:
    st.image("logo.png", width=180)
except Exception:
    st.markdown("### 💅 **NAN STUDIO TECH**")

st.markdown('<span class="badge">SISTEMA EXCLUSIVO PARA NAIL ARTISTS</span>', unsafe_allow_html=True)
st.title("Deja de perder 2 horas al día contestando precios por DM")
st.subheader("Tu propia página de citas que manda clientas listas para pagar directo a tu WhatsApp 24/7.")

st.markdown("""
Mientras estás aplicando acrílico o descansando, tu link:
* Muestra tu menú completo con fotos y precios actualizados.
* Deja que la clienta escoja día y hora exacta.
* Redacta y le envía a tu WhatsApp la ficha lista para confirmar con anticipo.
""")

st.divider()

# DEMO VIVA E INTERACTIVA
st.markdown("### 📱 Pruébalo tú misma (Demo en vivo)")
st.caption("Prueba cómo agendaría una clienta en tu futuro link:")

with st.container():
    st.markdown('<div class="demo-box">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        servicio = st.selectbox(
            "Servicio a realizar:",
            [
                "Uñas Acrílicas Esculpidas ($450)",
                "Retiro + Baño de Acrílico ($350)",
                "Gelish con Diseño Mano Alzada ($280)",
                "Efecto Espejo / Aurora ($320)"
            ]
        )
    with col2:
        fecha = st.date_input("Fecha preferida:", min_value=date.today())
        
    hora = st.selectbox(
        "Horario disponible:",
        ["11:00 AM", "1:30 PM", "4:00 PM", "6:30 PM"]
    )
    
    nombre_clienta = st.text_input("Nombre de la clienta:", "Valeria Gómez")
    
    # Generador de mensaje simulado
    mensaje_simulado = (
        f"¡Hola! Quiero agendar una cita.\n\n"
        f"👤 Nombre: {nombre_clienta}\n"
        f"💅 Servicio: {servicio}\n"
        f"📅 Fecha: {fecha.strftime('%d/%m/%Y')}\n"
        f"⏰ Horario: {hora}\n\n"
        f"¿Me pasas tus datos de transferencia para dejar el anticipo?"
    )
    
    link_demo = f"https://wa.me/525539233647?text={urllib.parse.quote(mensaje_simulado)}"
    
    st.markdown(f'''
    <a href="{link_demo}" target="_blank" style="display:block; background-color:#ff4b8b; color:white; padding:14px; text-align:center; font-size:16px; font-weight:bold; border-radius:8px; text-decoration:none; margin-top:12px;">
        ✨ Simular agendamiento (Ver mensaje en WhatsApp) →
    </a>
    ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# OFERTA Y LLAMADO A LA ACCIÓN
st.markdown("## ⚡ Te entrego tu link personalizado en 24 horas")
st.markdown("""
* **Tu enlace listo para poner en tu biografía de Instagram, TikTok o Facebook.**
* **Tus servicios, fotos y precios cargados.**
* **Tu número de WhatsApp configurado.**
* **Sin pagos mensuales de plataformas complicadas.**
""")

st.markdown("### Precio de lanzamiento: **$499 MXN** *(Pago único)*")

WHATSAPP = "525539233647"
msg_compra = "Hola Nancy, vi la app de agendas automáticas y quiero que me hagas mi link por $499."
link_compra = f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(msg_compra)}"

st.markdown(f'''
<a href="{link_compra}" target="_blank" style="display:block; background-color:#25D366; color:white; padding:20px; text-align:center; font-size:20px; font-weight:bold; border-radius:12px; text-decoration:none; margin: 25px 0;">
    💬 QUIERO MI AGENDA POR $499 MXN →
</a>
''', unsafe_allow_html=True)

st.caption("Nancy Rufino • Creadora de sistemas de citas para Nail Artists • CDMX")
