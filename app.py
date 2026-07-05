import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="BioPath-Sentinel AI", layout="centered")

# 2. ESTILO CSS
st.markdown("""
    <style>
    .stApp { background-color: #0b1120 !important; }
    h1, h2, h3, p, div { color: #e2e8f0 !important; }
    .main-title { color: #00f5d4 !important; font-size: 52px !important; font-weight: 800; text-align: center; margin-bottom: 5px; }
    .description { color: #f1f5f9 !important; font-size: 20px !important; line-height: 1.6; text-align: center; background-color: #1e293b !important; padding: 20px; border-radius: 15px; border: 1px solid #334155; }
    div.stDownloadButton > button { background-color: #00f5d4 !important; color: #000000 !important; font-weight: bold !important; border: none !important; }
    .header-style { color: #22d3ee !important; font-size: 32px !important; font-weight: 700; text-align: center; margin-top: 40px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Contenido
st.markdown('<p class="main-title">BioPath-Sentinel AI</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 26px;">Inteligencia Clínica para el Personal de Salud</p>', unsafe_allow_html=True)

st.markdown("""
<div class="description">
Tamizaje predictivo, gestión clínica hospitalaria y vigilancia genómica.<br>
<b>Soluciones diseñadas para médicos, enfermeros, nutricionistas e IPS.</b>
</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown('<p style="text-align: center; color: #94a3b8; font-size: 16px;">Haz clic aquí para descargar nuestra presentación en PDF</p>', unsafe_allow_html=True)

# 4. Botón de descarga (Solo una vez)
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

