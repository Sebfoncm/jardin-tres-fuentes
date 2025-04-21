import streamlit as st
import random
from datetime import datetime

# === FUNCIONES ===

def elegir_modo():
    return st.radio("🧭 ¿Cómo quieres que te hable hoy?", ["🌿 Compasivo", "🔥 Crudo"], horizontal=True)

def elegir_clima():
    return st.selectbox("¿Cómo te sientes hoy?", ["Soleado ☀️", "Nublado 🌥", "Tormenta ⛈", "Calma 🌿"])

def pregunta_estoica(modo):
    if modo == "🔥 Crudo":
        return random.choice([
            "¿Dejas que tu flojera dirija tu vida? ¿O tomas el timón con virtud?",
            "¿Estás viviendo de acuerdo con tus principios o solo sobreviviendo?",
            "¿De verdad crees que tendrás otra vida más tarde para empezar a actuar?"
        ])
    return random.choice([
        "¿Qué está en tus manos hoy, y qué no?",
        "¿Estás actuando conforme a tu virtud o a tus impulsos?",
        "¿Qué harías si este fuera tu último día?"
    ])

def conversacion_con_la_sombra(modo):
    if modo == "🔥 Crudo":
        return "🔥 Lo que más criticas en otros probablemente vive en ti. Míralo de frente. No huyas."
    return "🌑 ¿Qué crítica hacia otros podrías estar proyectando desde ti mismo? Obsérvalo sin juicio."

def arquetipo_del_dia():
    return random.choice([
        "🧙 Hoy te acompaña el Sabio: busca entender más allá de lo aparente.",
        "🛡 Hoy te guía el Guerrero: actúa con coraje y determinación.",
        "💞 Hoy está presente el Amante: cultiva lo que amas con profundidad."
    ])

def bitacora_final(pregunta, sombra, arquetipo):
    st.markdown("### ✍️ Bitácora interna")
    reflexion = st.text_area("¿Qué te deja esta sesión?")
    if st.button("Guardar entrada"):
        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f"bitacora_{fecha}.txt", "w", encoding="utf-8") as f:
            f.write("🌱 Jardín de las Tres Fuentes Internas\n")
            f.write(f"Fecha: {fecha}\n\n")
            f.write(f"Pregunta estoica: {pregunta}\n")
            f.write(f"Sombra: {sombra}\n")
            f.write(f"Arquetipo: {arquetipo}\n")
            f.write(f"Reflexión escrita: {reflexion}")
        st.success("Bitácora guardada localmente ✅")

# === APP ===

st.title("🌿 Jardín de las Tres Fuentes Internas")
st.caption("Estoicismo · Budismo · Psicología Junguiana")

modo = elegir_modo()
clima = elegir_clima()

st.divider()
st.subheader("🌱 Tu sesión de hoy:")

pregunta = pregunta_estoica(modo)
sombra = conversacion_con_la_sombra(modo)
arquetipo = arquetipo_del_dia()

st.markdown(f"**1. Pregunta estoica:** {pregunta}")
st.markdown(f"**2. Conversación con la sombra:** {sombra}")
st.markdown(f"**3. Arquetipo del día:** {arquetipo}")

bitacora_final(pregunta, sombra, arquetipo)

st.divider()
st.caption("Creado por Sebastián Foncillas 🧠")
