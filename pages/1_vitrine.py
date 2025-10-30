import streamlit as st

df = st.session_state['df']

st.write("# Vitrine")

st.write(df)

n = 4
cols = st.columns(n)
for indice, pokemon in df.iterrows():
    with cols[indice % n].container(border=True):
        st.image(pokemon['Image'])
        st.write(f"{pokemon['Name']}")
