import streamlit as st

def go_to_page():
    pass

with st.container():
    st.image(
        'assets./perfil.png'
    )

    st.text_input(
        label = "Email"
    )

    st.text_input(
        label = "Senha"
    )

    col1, col2 = st.columns(2)
    with col1:
        st.button(
            label="Cadastre-se"
        )

    with col2:
        st.button(
            label="Entrar"
        )

st.sidebar.title("Navegação")