import streamlit as st

st.set_page_config(page_title="BioPath Sentinel AI", layout="centered")

st.title("BioPath Sentinel AI")
st.subheader("Inteligencia Clínica para el Personal de Salud")

st.markdown("""
Tamizaje predictivo, gestión clínica hospitalaria y vigilancia genómica.  
Soluciones diseñadas para médicos, enfermeros, nutricionistas e IPS.
""")

# Botón de descarga del PDF
with open("BioPath_Sentinel_AI_InA.pdf", "rb") as pdf_file:
    pdf_bytes = pdf_file.read()
    st.download_button(
        label="Descargar PDF",
        data=pdf_bytes,
        file_name="BioPath_Sentinel_AI_InA.pdf",
        mime="application/pdf"
    )

st.markdown("---")
st.header("Videos de la Startup")

st.subheader("Video 1: Presentación")
st.video("https://www.youtube.com/watch?v=TuVideoID1")

st.subheader("Video 2: Demo Técnica")
st.video("https://www.youtube.com/watch?v=TuVideoID2")
