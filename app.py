import streamlit as st
import pandas as pd

st.write("# Pokedex")

df = pd.read_csv("https://raw.githubusercontent.com/Assaoka/Decolar--Introducao_a_Ciencia_de_Dados/refs/heads/main/pokemon.csv")


with st.sidebar:
    st.multiselect(
        label="Tipos",
        options=df['Primary Typing'].unique(),
        key="filtro"
    )

st.button(label="Botão", key="b1")
if st.session_state['b1']:
    st.write("Voce clicou")

df = df[df['Primary Typing'].isin(st.session_state['filtro'])]
st.session_state['df'] = df

st.navigation([
	st.Page("pages/1_vitrine.py", title="Vitrine", icon="🐉"),
	st.Page("pages/2_dashboard.py", title="Dashboard de Análise", icon="📊")
]).run()

