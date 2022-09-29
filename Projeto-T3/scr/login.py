import streamlit as st

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

def go_to_page():
    pass

with st.container():
    st.image(
        image = '../assets/perfil.png'
    )

    st.text_input(
        label = "Email",
        placeholder = "Digite aqui seu email"
    )

    st.text_input(
        label = "Senha",
        placeholder = "Digite aqui sua senha"
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
