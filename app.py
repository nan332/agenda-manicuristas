import streamlit as st
import urllib.parse

st.set_page_config(page_title="Agendas para Manicuristas", page_icon="💅", layout="centered")

TU_WHATSAPP = "525539233647"

st.title("💅 ¿Pones uñas y pierdes clientas por WhatsApp?")
st.subheader("Yo te pongo tu agenda automática que trabaja 24/7")
st.divider()

st.write("✅ Tu clienta ve tus precios y aparta SOLA")
st.write("✅ Te llega directo a tu WhatsApp sin preguntar")
st.write("✅ Ya no contestas 100 mensajes para agendar 2")

st.divider()
st.header("🎬 Pruébala aquí mismo:")
with st.form("demo"):
    nombre = st.text_input("Nombre de tu clienta")
    servicio = st.selectbox("Servicio", ["Acrílicas $350", "Gelish $200", "Soft Gel $400"])
    fecha = st.date_input("Fecha")
    if st.form_submit_button("PROBAR COMO CLIENTA"):
        st.success(f"Así te llegaría: {nombre} quiere {servicio} el {fecha}")
        st.balloons()

st.divider()
st.header("💰 ¿Cuánto cuesta tener la tuya?")
st.success("SETUP: $799 MXN - Te la entrego con tu nombre en 24h")
st.warning("MANTENIMIENTO: $199/mes - Yo la mantengo prendida")

st.divider()
st.header("👉 ¿Quieres tu demo gratis?")
nombre_mani = st.text_input("Escribe tu nombre o tu salón", placeholder="Ej: Nails by Nancy")
if nombre_mani:
    mensaje = f"Hola Nancy! Soy {nombre_mani}, pongo uñas y quiero mi demo gratis de agenda. Vi tu pagina."
    mensaje_encoded = urllib.parse.quote(mensaje)
    link_wa = f"https://wa.me/{TU_WHATSAPP}?text={mensaje_encoded}"
    st.link_button("📲 QUIERO MI DEMO GRATIS POR WHATSAPP", link_wa, type="primary", use_container_width=True)

st.caption("Creado por Nancy | Agendas Automaticas CDMX")
