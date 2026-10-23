import streamlit as st
import urllib.parse

# 1. Configuración de página de Streamlit
st.set_page_config(
    page_title="NAN STUDIO",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Configura tu número de WhatsApp aquí (con lada, sin espacios ni guiones)
mi_numero_whatsapp = "525539233647"

# 3. Mensajes predeterminados para la demo y el botón de compra
texto_whatsapp_sistema = urllib.parse.quote("Hola NAN STUDIO 👋. Vi su sistema de agenda automática para manicuristas y quiero el mío por $499 MXN.")

# 4. Diseño HTML/CSS ultra-exclusivo móvil "inyectado" de forma segura en Streamlit
diseno_completo = f"""
<style>
    /* Ocultar elementos sobrantes de Streamlit */
    #MainMenu, footer, header {{visibility: hidden !important;}}
    .block-container {{
        padding: 0px !important;
        max-width: 440px !important;
        margin: auto;
    }}
    
    /* El cuerpo principal se convierte en el teléfono oscuro */
    .stApp {{
        background-color: #000000 !important;
    }}
    
    /* Contenedor del Mockup Móvil Premium */
    .movil-wrapper {{
        background: radial-gradient(135deg, #100f0e 0%, #070706 100%);
        border: 1px solid rgba(212, 175, 55, 0.15);
        border-radius: 40px;
        padding: 30px 24px;
        margin: 15px auto;
        box-shadow: 0px 25px 50px -12px rgba(0, 0, 0, 0.9), 0px 0px 30px rgba(212, 175, 55, 0.05);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #e5e5e5;
    }}
    
    /* Placa Dorada Premium para NAN */
    .placa-oro {{
        display: block;
        width: 140px;
        margin: 0 auto 15px auto;
        border: 2px solid #d4af37;
        padding: 10px 0;
        text-align: center;
        background: linear-gradient(135deg, #1c150c 0%, #0d0a06 100%);
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.1), inset 0 0 8px rgba(212, 175, 55, 0.2);
    }}
    
    .logo-nan {{
        font-family: 'Cinzel', 'Times New Roman', serif;
        font-size: 34px;
        font-weight: 800;
        color: transparent;
        background: linear-gradient(90deg, #ffe58f 0%, #d4af37 50%, #aa771c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 4px;
        margin: 0;
        line-height: 1;
    }}
    
    .texto-sub-nan {{
        color: #d4af37;
        font-size: 11px;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        margin: 18px 0 25px 0;
        text-align: center;
        font-weight: 600;
    }}
    
    /* Caja de impacto 24/7 */
    .caja-impacto {{
        border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 18px;
        background: linear-gradient(180deg, rgba(20, 18, 16, 0.7) 0%, rgba(10, 9, 8, 0.9) 100%);
        padding: 22px 18px;
        margin-bottom: 25px;
        display: flex;
        gap: 16px;
        align-items: center;
    }}
    
    .icono-caja {{
        font-size: 32px;
        color: #d4af37;
    }}
    
    .texto-caja {{
        font-size: 16px;
        line-height: 1.4;
        font-weight: 700;
        color: #ffffff;
    }}
    
    /* Lista de beneficios */
    .beneficio-lista {{
        margin-bottom: 30px;
    }}
    
    .beneficio-item {{
        display: flex;
        align-items: flex-start;
        gap: 14px;
        margin-bottom: 22px;
    }}
    
    .circulo-check {{
        min-width: 20px;
        height: 20px;
        border-radius: 50%;
        border: 1px solid #d4af37;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #d4af37;
        font-size: 10px;
        margin-top: 2px;
        font-weight: bold;
    }}
    
    .beneficio-texto {{
        font-size: 14.5px;
        line-height: 1.4;
        color: #bfa88f;
        font-weight: 500;
    }}
    
    .beneficio-destaque {{
        color: #ffffff;
        font-weight: 700;
    }}
    
    /* Detalles de Precio y Oferta */
    .precio-bloque {{
        background: rgba(212, 175, 55, 0.05);
        border: 1px dashed rgba(212, 175, 55, 0.2);
        border-radius: 14px;
        padding: 15px;
        text-align: center;
        margin-bottom: 20px;
    }}
    
    .precio-texto {{
        font-size: 17px;
        color: #ffffff;
        font-weight: 700;
        margin-bottom: 4px;
    }}
    
    .precio-monto {{
        color: #d4af37;
        font-size: 22px;
        font-weight: 800;
    }}
    
    /* Botón verde neón de WhatsApp */
    .btn-conexion-ws {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        background-color: #25d366;
        color: #ffffff !important;
        text-decoration: none !important;
        font-size: 17px;
        font-weight: 700;
        padding: 16px;
        border-radius: 30px;
        box-shadow: 0px 8px 20px rgba(37, 211, 102, 0.35);
        transition: all 0.2s ease;
        margin-bottom: 18px;
        border: none;
    }}
    
    .btn-conexion-ws:hover {{
        transform: scale(1.02);
        box-shadow: 0px 10px 25px rgba(37, 211, 102, 0.5);
    }}
    
    .icono-ws {{
        width: 22px;
        height: 22px;
    }}
    
    /* Garantía */
    .textos-pequenos {{
        font-size: 11px;
        color: #706860;
        text-align: center;
        line-height: 1.5;
        margin-bottom: 30px;
    }}
    
    .separador {{
        width: 60px;
        height: 1px;
        background-color: rgba(212, 175, 55, 0.3);
        margin: 20px auto;
    }}
    
    .autor-footer {{
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #4a453f;
        text-align: center;
    }}
</style>

<div class="movil-wrapper">
    <!-- Placa de lujo superior -->
    <div class="placa-oro">
        <h1 class="logo-nan">NAN</h1>
    </div>
    <div class="texto-sub-nan">AGENDA AUTOMÁTICA</div>
    
    <!-- Propuesta de Valor -->
    <div class="caja-impacto">
        <div class="icono-caja">🗓️✨</div>
        <div class="texto-caja">Para que agende sola y le caigan clientas a su WhatsApp 24/7</div>
    </div>
    
    <!-- Beneficios (Círculos dorados) -->
    <div class="beneficio-lista">
        <div class="beneficio-item">
            <div class="circulo-check">✓</div>
            <div class="beneficio-texto"><span class="beneficio-destaque">Responde al instante</span> a tus clientas.</div>
        </div>
        <div class="beneficio-item">
            <div class="circulo-check">✓</div>
            <div class="beneficio-texto"><span class="beneficio-destaque">Confirma y recuerda citas</span> de forma 100% automática.</div>
        </div>
        <div class="beneficio-item">
            <div class="circulo-check">✓</div>
            <div class="beneficio-texto"><span class="beneficio-destaque">Capta más clientas</span> desde tus redes sociales (Instagram, TikTok) directo a tu WhatsApp.</div>
        </div>
        <div class="beneficio-item">
            <div class="circulo-check">✓</div>
            <div class="beneficio-texto">Tus <span class="beneficio-destaque">servicios, precios, días y horarios</span> listos en tu enlace.</div>
        </div>
    </div>
    
    <!-- Bloque de Precio -->
    <div class="precio-bloque">
        <div class="precio-texto">Inversión única (sin mensualidades):</div>
        <div class="precio-monto">$499 MXN</div>
    </div>
    
    <!-- Botón directo -->
    <a href="https://wa.me/{mi_numero_whatsapp}?text={texto_whatsapp_sistema}" target="_blank" class="btn-conexion-ws">
        <!-- SVG de WhatsApp integrado -->
        <svg class="icono-ws" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12.031 6c-2.767 0-5 2.233-5 5c0 1.054.325 2.031.881 2.844L7.094 16.938l3.188-.813c.781.422 1.672.688 2.594.688 2.767 0 5-2.234 5-5c-.001-2.767-2.234-5-5-5zm3.172 6.906c-.125.359-.734.688-1.016.719-.281.031-.563.047-.844-.047-.188-.063-.422-.156-.703-.266-1.188-.484-1.953-1.688-2.016-1.766-.063-.078-.5-.656-.5-1.25s.313-.891.422-1c.109-.109.25-.172.375-.172.063 0 .125 0 .188.016.078.016.156.016.234.203.094.219.328.797.359.859.031.063.047.141 0 .234-.047.094-.078.156-.156.25-.078.094-.156.156-.219.234-.078.078-.156.172-.063.328.094.156.406.672.875 1.094.594.547 1.094.719 1.25.797.156.078.25.063.344-.047.094-.109.406-.484.516-.656.109-.172.219-.141.359-.094.141.047.906.422 1.063.5.156.078.266.125.313.203.046.062.046.359-.079.718z"/>
        </svg>
        Conectar mi WhatsApp
    </a>
    
    <!-- Detalles de garantía -->
    <div class="textos-pequenos">
        Entrega en menos de 24 horas • Configuración fácil y personalizada • Sin complicaciones.
        <div class="separador"></div>
        <div class="autor-footer">NAN STUDIO • Automatiza tu agenda de uñas</div>
    </div>
</div>
"""

# 5. Renderizar en pantalla de Streamlit
st.markdown(diseno_completo, unsafe_allow_html=True)
