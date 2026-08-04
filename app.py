"""
app.py
------
Examen Práctico: Agente de IA con LM Studio y Streamlit
Estudiante: Edy Martinez

Aplicación web en Streamlit que consulta a un modelo Instruct liviano
(Llama 3.2 1B/3B, Qwen2.5 1.5B/3B, Phi-3 Mini o similar) ejecutado
localmente en LM Studio, para responder preguntas académicas sobre
tecnología, programación o inteligencia artificial.
"""

import streamlit as st
from openai import OpenAI

# ----------------------------------------------------------------------
# Configuración de conexión a LM Studio (servidor local, API tipo OpenAI)
# ----------------------------------------------------------------------
LM_STUDIO_BASE_URL = "http://localhost:1234/v1"
LM_STUDIO_API_KEY = "lm-studio"  # LM Studio no valida esta clave

# System Prompt: define el comportamiento del agente
SYSTEM_PROMPT = (
    "Eres un agente tutor académico especializado en tecnología, "
    "programación e inteligencia artificial. Cuando el usuario pregunte "
    "sobre un concepto, responde siempre en español y en este orden:\n"
    "1. Explica el concepto de forma clara y sencilla.\n"
    "2. Proporciona un ejemplo concreto.\n"
    "3. Menciona una aplicación práctica del concepto en el mundo real.\n"
    "4. Finaliza con una pregunta de comprobación para verificar que el "
    "usuario entendió el tema.\n"
    "Si la pregunta no está relacionada con tecnología, programación o "
    "inteligencia artificial, indícalo amablemente y pide una pregunta "
    "sobre esos temas."
)

st.set_page_config(
    page_title="Agente de IA - Examen Práctico",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 Agente de IA Académico")
st.write(
    "Este agente responde preguntas académicas sobre **tecnología, "
    "programación e inteligencia artificial**, usando un modelo Instruct "
    "liviano ejecutado localmente con **LM Studio**. Cada respuesta incluye "
    "una explicación, un ejemplo, una aplicación práctica y una pregunta "
    "de comprobación."
)

with st.sidebar:
    st.subheader("Configuración del modelo")
    modelo = st.text_input(
        "Identificador del modelo en LM Studio",
        value="qwen2.5-1.5b-instruct",
        help=(
            "Debe coincidir exactamente con el nombre del modelo cargado "
            "en LM Studio (pestaña Developer / Local Server)."
        ),
    )
    st.caption(f"Endpoint: {LM_STUDIO_BASE_URL}")

consulta = st.text_area(
    "Escribe tu consulta académica",
    placeholder="Ejemplo: ¿Qué es una red neuronal?",
    height=100,
)

if st.button("Consultar al Agente", type="primary"):
    if not consulta.strip():
        st.warning("Por favor escribe una consulta antes de continuar.")
    else:
        with st.spinner("El agente está pensando..."):
            try:
                cliente = OpenAI(
                    base_url=LM_STUDIO_BASE_URL,
                    api_key=LM_STUDIO_API_KEY,
                )
                respuesta = cliente.chat.completions.create(
                    model=modelo,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": consulta},
                    ],
                    temperature=0.6,
                    max_tokens=700,
                )
                contenido = respuesta.choices[0].message.content
                st.subheader("Respuesta del agente")
                st.markdown(contenido)
            except Exception as error:
                st.error(
                    "No fue posible conectar con LM Studio. Verifica que:\n\n"
                    "- LM Studio esté abierto.\n"
                    "- El modelo indicado en la barra lateral esté cargado.\n"
                    "- El servidor local esté iniciado (Developer → Start "
                    "Server) en el puerto 1234.\n\n"
                    f"Detalle técnico: {error}"
                )

st.divider()
st.caption("Examen Práctico · Agente de IA con LM Studio y Streamlit · Edy Martinez")
