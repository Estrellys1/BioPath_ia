import streamlit as st

# Configuración inicial de la página
st.set_page_config(page_title="BioPath-Sentinel AI", layout="centered")

# CSS optimizado para el modo oscuro definido en config.toml
st.markdown("""
    <style>
    /* Forzar fondo oscuro en toda la página */
    .stApp {
        background-color: #000000 !important;
    }
    /* Asegurar que todos los textos sean claros */
    h1, h2, h3, p, div {
        color: #ffffff !important;
    }
    .main-title {
        color: #00f5d4 !important; 
        font-size: 52px !important;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
    }
    .description {
        color: #f1f5f9 !important;
        font-size: 20px !important;
        line-height: 1.6;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
    .header-style {
        color: #22d3ee !important;
        font-size: 32px !important;
        font-weight: 700;
        text-align: center;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Títulos y Descripción
st.markdown('<p class="main-title">BioPath-Sentinel AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Inteligencia Clínica para el Personal de Salud</p>', unsafe_allow_html=True)

st.markdown("""
<div class="description">
Tamizaje predictivo, gestión clínica hospitalaria y vigilancia genómica.<br>
<b>Soluciones diseñadas para médicos, enfermeros, nutricionistas e IPS.</b>
</div>
""", unsafe_allow_html=True)

st.write("")

# Botón de descarga
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        with open("BioPath_Sentinel_AI_InA.pdf", "rb") as pdf_file:
            st.markdown("""
    <style>
    /* Estilos globales */
    .stApp {
        background-color: #000000 !important;
    }
    h1, h2, h3, p, div {
        color: #ffffff !important;
    }
    .main-title {
        color: #00f5d4 !important; 
        font-size: 52px !important;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
    }
    .description {
        color: #f1f5f9 !important;
        font-size: 20px !important;
        line-height: 1.6;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
    }
    
    /* ESTO ES LO QUE TE FALTABA - Estilo para el botón */
    div.stDownloadButton > button {
        background-color: #00f5d4 !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: none !important;
    }
    except FileNotFoundError:
        st.warning("Archivo de presentación no disponible.")

st.markdown("---")

# Secciones de video con diseño mejorado
st.markdown('<p class="header-style">AI-Powered Clinical Intelligence</p>', unsafe_allow_html=True)

st.subheader("BioPath-Sentinel AI | Company Overview")
st.video("https://www.youtube.com/watch?v=TuVideoID1")

st.write("---")

st.subheader("Artificial Intelligence • Bioinformatics • Digital Health")
st.video("https://www.youtube.com/watch?v=TuVideoID2")
