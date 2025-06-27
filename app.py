#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st

st.set_page_config(page_title="Chatbot Renovación Carnet", page_icon="🚗")

st.title("🤖 Chatbot: Certificado Médico para Carnet de Conducir")

# Simulación de datos por comunidad
centros = {
    "Madrid": ["Centro Médico Goya", "Clínica Reconduce", "Centro Sanitas Cuatro Caminos"],
    "Andalucía": ["Clínica Andalucía Conduce", "Centro Médico Sur", "Médicos Aljarafe"],
    "Cataluña": ["Médico Carnet BCN", "Clínica Diagonal Drive", "Centro Médico Gracia"]
}

# Estado de conversación
if "step" not in st.session_state:
    st.session_state.step = 1

def reiniciar_chat():
    st.session_state.step = 1
    st.session_state.comunidad = ""
    st.session_state.nombre = ""

# Paso 1: nombre del usuario
if st.session_state.step == 1:
    st.write("👋 ¡Hola! Soy tu asistente para renovar el carnet de conducir.")
    st.session_state.nombre = st.text_input("¿Cómo te llamas?")
    if st.session_state.nombre:
        st.session_state.step = 2
        st.experimental_rerun()

# Paso 2: comunidad autónoma
elif st.session_state.step == 2:
    st.write(f"Encantado, {st.session_state.nombre}.")
    st.session_state.comunidad = st.selectbox("¿En qué comunidad autónoma estás?", list(centros.keys()))
    if st.session_state.comunidad:
        st.session_state.step = 3
        st.experimental_rerun()

# Paso 3: Mostrar información relevante
elif st.session_state.step == 3:
    st.write(f"🔍 En {st.session_state.comunidad}, estos son los pasos para renovar tu carnet:")

    st.markdown("""
    1. **Solicita un certificado médico** en un centro autorizado.
    2. Lleva tu DNI/NIE y el carnet de conducir.
    3. Hazte una revisión (vista, reflejos, presión).
    4. Te entregarán el certificado directamente o lo enviarán a la DGT.
    5. **Precio estimado**: entre 30 € y 60 €.
    """)

    st.write("🏥 Centros médicos recomendados:")
    for c in centros[st.session_state.comunidad]:
        st.write(f"- {c}")

    if st.button("Finalizar"):
        st.session_state.step = 4
        st.experimental_rerun()

# Paso 4: Final
elif st.session_state.step == 4:
    st.success("✅ ¡Listo! Ya sabes cómo renovar tu carnet.")
    st.markdown("¿Quieres volver a empezar?")
    if st.button("🔄 Reiniciar"):
        reiniciar_chat()


