
import streamlit as st

st.set_page_config(page_title="Chatbot Renovación Carnet", page_icon="🚗")
st.title("🤖 Chatbot: Certificado Médico para Carnet de Conducir")

# Simulación de datos por comunidad
centros = {
    "Madrid": ["Centro Médico Goya", "Clínica Reconduce", "Centro Sanitas Cuatro Caminos"],
    "Andalucía": ["Clínica Andalucía Conduce", "Centro Médico Sur", "Médicos Aljarafe"],
    "Cataluña": ["Médico Carnet BCN", "Clínica Diagonal Drive", "Centro Médico Gracia"]
}

def generar_resumen(nombre, comunidad, edad, renovar_tipo):
    texto = f"""
Hola {nombre},

Estos son los pasos para renovar tu carnet de tipo {renovar_tipo} en {comunidad}:

1. Solicita un certificado médico en un centro autorizado.
2. Lleva tu DNI/NIE y tu carnet de conducir actual.
3. Te harán una revisión médica (vista, coordinación, presión arterial).
4. El centro enviará tu certificado a la DGT o te lo entregará.
5. Precio estimado: entre 30 € y 60 €.

🏥 Centros recomendados en {comunidad}:
"""
    for c in centros[comunidad]:
        texto += f"- {c}\n"

    if edad >= 65:
        texto += "\n📢 Nota: Como tienes más de 65 años, la validez del carnet puede ser menor.\n"

    return texto

def show_form():
    with st.form("chatbot_form"):
        nombre = st.text_input("¿Cómo te llamas?", max_chars=50)
        comunidad = st.selectbox("¿En qué comunidad autónoma estás?", list(centros.keys()))
        edad = st.slider("¿Cuál es tu edad?", 16, 100, 30)
        renovar_tipo = st.selectbox("¿Qué tipo de carnet quieres renovar?", ["B (coche)", "A (moto)", "C (camión)", "D (autobús)"])
        submitted = st.form_submit_button("Consultar pasos")

    if submitted:
        if not nombre.strip():
            st.error("Por favor, introduce tu nombre.")
        else:
            resumen = generar_resumen(nombre, comunidad, edad, renovar_tipo)
            st.success("✅ Consulta generada correctamente.")
            st.text_area("Resumen personalizado:", resumen, height=300)

            # Convertir a bytes para el botón de descarga
            resumen_bytes = resumen.encode("utf-8")

            st.download_button(
                label="📄 Descargar resumen como TXT",
                data=resumen_bytes,
                file_name=f"renovacion_{nombre.lower().replace(' ', '_')}.txt",
                mime="text/plain"
            )

show_form()
