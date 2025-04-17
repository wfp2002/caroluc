import streamlit as st
import random
import time

st.set_page_config(page_title="Jogo Lucas vs Carol", layout="centered")

# Fundo estilizado e demais CSS
st.markdown("""
    <style>
        body {
            background-color: #121212;
        }
        .stApp {
            background: linear-gradient(to bottom, #0f2027, #203a43, #2c5364);
            color: white;
        }
        .title {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            margin-top: 30px;
            color: #00FFAA;
        }
        .name {
            text-align: center;
            font-size: 80px;
            font-weight: bold;
            margin-top: 30px;
        }
        .lucas {
            color: #00BFFF;
        }
        .carol {
            color: #FF69B4;
        }
        .contador {
            text-align: center;
            font-size: 30px;
            margin-top: 20px;
            color: #FFA500;
        }
        .parabens {
            text-align: center;
            font-size: 50px;
            margin-top: 40px;
            color: #FFD700;
            font-weight: bold;
        }
        div.stButton > button {
            display: block;
            margin: 0 auto;
            padding: 1em 2em;
            font-size: 25px;
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Lucas vs Carol</div>", unsafe_allow_html=True)

# Espaços reservados para os elementos dinâmicos
contador_placeholder = st.empty()
nome_placeholder = st.empty()
progress_bar = st.progress(0)
final_placeholder = st.empty()

# Botão de iniciar
if st.button("🎮 Iniciar"):
    total_rodadas = 30
    ultimo_nome = ""

    for i in range(total_rodadas):
        restantes = total_rodadas - i
        contador_placeholder.markdown(f"<div class='contador'>Faltam {restantes} rodada{'s' if restantes > 1 else ''}...</div>", unsafe_allow_html=True)

        resultado = random.randint(0, 1)
        if resultado == 1:
            ultimo_nome = "Lucas"
            nome_placeholder.markdown("<div class='name lucas'>Lucas</div>", unsafe_allow_html=True)
        else:
            ultimo_nome = "Carol"
            nome_placeholder.markdown("<div class='name carol'>Carol</div>", unsafe_allow_html=True)

        progress_bar.progress((i + 1) / total_rodadas)
        time.sleep(0.5)

    # Mostra o campeão com parabéns
    final_placeholder.markdown(f"<div class='parabens'>🎉 Parabéns, {ultimo_nome}!</div>", unsafe_allow_html=True)
