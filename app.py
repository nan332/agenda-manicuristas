import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="NAN Studio Tech", page_icon="👑", layout="centered")

# Lee y proyecta el diseño con todas sus funciones
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=950, scrolling=True)
