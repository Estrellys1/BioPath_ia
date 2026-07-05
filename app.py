import streamlit as st

st.set_page_config(page_title="BioPath Sentinel AI", layout="centered")

# CSS personalizado para colores y tamaños
st.markdown("""
    <style>
    .main-title {
        color: #00f5d4; /* Color cian */
        font-size: 50px !important;
        font-weight: 800;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-title {
        color: #ffffff;
        font-size: 24px !important;
        text-align: center;
        margin-bottom: 30px;
    }
    .description {
        color: #e0e0e0;
        font-size: 18px !important;
        line-height: 1.6;
        text-align: center;
    }
    .header-style {
        color: #22d3ee;
        font-size: 30px !important;
        margin-top: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# Uso del HTML personalizado
st.markdown('<p class="main-title">BioPath Sentinel AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Inteligencia Clínica para el Personal de Salud</p>', unsafe_allow_html=True)

st.markdown("""
<div class="description">
Tamizaje predictivo, gestión clínica hospitalaria y vigilancia genómica.<br>
<b>Soluciones diseñadas para médicos, enfermeros, nutricionistas e IPS.</b>
</div>
""", unsafe_allow_html=True)

st.write("") # Espacio en blanco

# Botón de descarga centrado
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        with open("BioPath_Sentinel_AI_InA.pdf", "rb") as pdf_file:
            st.download_button(
                label="Descargar Presentación PDF",
                data=pdf_file,
                file_name="BioPath_Sentinel_AI_InA.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.error("El archivo PDF no se encuentra en la ruta especificada.")

st.markdown("---")
st.markdown('<p class="header-style">AI-Powered Clinical Intelligence</p>', unsafe_allow_html=True)

st.write("### BioPath Sentinel AI | Company Overview")
st.video("https://www.youtube.com/watch?v=TuVideoID1")

st.write("### Artificial Intelligence • Bioinformatics • Digital Health")
st.video("https://www.youtube.com/watch?v=TuVideoID2")
