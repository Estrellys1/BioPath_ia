import streamlit as st

st.set_page_config(page_title="BioPath Sentinel AI", layout="centered")

# CSS personalizado
st.markdown("""
<style>

.main-title{
    color:#0057D9;
    font-size:64px;
    font-weight:800;
    margin-bottom:5px;
}

.sub-title{
    color:#0057D9;
    font-size:40px;
    font-weight:700;
    margin-bottom:20px;
}

.texto{
    font-size:24px;
    color:#333333;
    line-height:1.6;
}

</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown(
    '<div class="main-title">BioPath Sentinel AI</div>',
    unsafe_allow_html=True
)

# Subtítulo
st.markdown(
    '<div class="sub-title">Inteligencia Clínica para el Personal de Salud</div>',
    unsafe_allow_html=True
)

# Descripción
st.markdown(
    """
    <div class="texto">
    Tamizaje predictivo, gestión clínica hospitalaria y vigilancia genómica.<br><br>
    Soluciones diseñadas para médicos, enfermeros, nutricionistas e IPS.
    </div>
    """,
    unsafe_allow_html=True
)

# Botón de descarga
with open("BioPath_Sentinel_AI_InA.pdf", "rb") as pdf_file:
    pdf_bytes = pdf_file.read()

st.download_button(
    label="📄 Descargar PDF",
    data=pdf_bytes,
    file_name="BioPath_Sentinel_AI_InA.pdf",
    mime="application/pdf"
)

st.markdown("---")

st.header("Videos de la Startup")

st.subheader("Video 1: BioPath Sentinel AI | Company Overview")
st.video("https://www.youtube.com/watch?v=O6K29nUL0iY")

st.subheader("Video 2: BioPath Sentinel AI | AI for Healthcare & Bioinformatics")
st.video("https://www.youtube.com/watch?v=TGPN6YK09yc")
