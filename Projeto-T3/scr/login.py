import streamlit as st

# with open("style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

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

    st.button(
            label="Cadastre-se"
        )
    st.button(
            label="Entrar"
        )
