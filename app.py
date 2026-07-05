import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="BioPath-Sentinel AI", layout="centered")

# 2. ESTILO CSS: Este bloque va al principio, fuera de cualquier 'with' o 'try'
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    h1, h2, h3, p, div { color: #ffffff !important; }
    .main-title { color: #00f5d4 !important; font-size: 52px !important; font-weight: 800; text-align: center; margin-bottom: 5px; }
    .description { color: #f1f5f9 !important; font-size: 20px !important; line-height: 1.6; text-align: center; background-color: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 15px; }
    div.stDownloadButton > button { background-color: #00f5d4 !important; color: #000000 !important; font-weight: bold !important; border: none !important; }
    .header-style { color: #22d3ee !important; font-size: 32px !important; font-weight: 700; text-align: center; margin-top: 40px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Contenido de la página
st.markdown('<p class="main-title">BioPath-Sentinel AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title" style="text-align: center; font-size: 26px;">Inteligencia Clínica para el Personal de Salud</p>', unsafe_allow_html=True)

st.markdown("""
<div class="description">
Tamizaje predictivo, gestión clínica hospitalaria y vigilancia genómica.<br>
<b>Soluciones diseñadas para médicos, enfermeros, nutricionistas e IPS.</b>
</div>
""", unsafe_allow_html=True)

st.write("") 

# Modifica la sección del botón en tu app.py así:

st.write("") 
# Nueva línea con la instrucción para el usuario
st.markdown('<p style="text-align: center; color: #94a3b8; font-size: 16px;">Haz clic aquí para descargar nuestra presentación en PDF</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        with open("BioPath_Sentinel_AI_InA.pdf", "rb") as pdf_file:
            st.download_button(
                label="Descargar Presentación",
                data=pdf_file,
                file_name="BioPath_Sentinel_AI_InA.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning("Archivo de presentación no disponible.")

# 4. Botón de descarga (Ahora sí, dentro de su columna)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        with open("BioPath_Sentinel_AI_InA.pdf", "rb") as pdf_file:
            st.download_button(
                label="Descargar Presentación",
                data=pdf_file,
                file_name="BioPath_Sentinel_AI_InA.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning("Archivo de presentación no disponible.")

st.markdown("---")

# 5. Videos
st.markdown('<p class="header-style">AI-Powered Clinical Intelligence</p>', unsafe_allow_html=True)
st.subheader("BioPath-Sentinel AI | Company Overview")
st.video("https://www.youtube.com/watch?v=TuVideoID1")

st.write("---")
st.subheader("Artificial Intelligence • Bioinformatics • Digital Health")
st.video("https://www.youtube.com/watch?v=TuVideoID2")
