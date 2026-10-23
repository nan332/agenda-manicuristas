import streamlit as st
import urllib.parse

st.set_page_config(page_title="NAN - Agendas Automaticas", page_icon="logo.png", layout="centered")

# LOGO DE LUJO NEGRO Y DORADO
st.image("logo.png", width=220)

WHATSAPP = "525539233647"

st.title("Yo le hago su Agenda Automática a Manicuristas 💅")
st.markdown("### Para que agenda sola y le caigan clientas a su WhatsApp 24/7")

st.markdown("""
**Yo no hago uñas. Yo hago el sistema.**

Yo les creo su link para que su clienta aparte SOLA y a ellas les llegue a su WhatsApp lista para cobrar.

Dejan de perder tiempo contestando mensajes.
""")
st.divider()
st.markdown("**Demo de lo que les entrego:**")
with st.container(border=True):
    st.text_input("Nombre", "Lupita", disabled=True)
    st.button("Apartar cita", disabled=True)

st.divider()
st.markdown("## $499 pago único - Se la hago en 24hrs")
msg = "Hola Nancy quiero que me hagas mi agenda $499"
link = f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(msg)}"
st.link_button("QUIERO QUE ME HAGAS MI AGENDA →", link)
st.caption("Soy Nancy - Hago agendas, no hago uñas - 55 3923 3647")
