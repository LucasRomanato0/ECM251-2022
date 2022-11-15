import streamlit as st
from src.modules.user import User
from src.controllers.user_controller import UserController
import time

controller = UserController()

def autentication_user(username, password, aut):
    if aut == "Cadastro":
        st.session_state["message"] = "Bem Vindo!"
    else:
        usuario = controller.get_user(username=username)
        if usuario != None and username == usuario.username and password == usuario.password:
            st.session_state["message"] = f'Bem vindo, {usuario.name}! Ótimas compras!'
            st.session_state["hello"] = usuario.name
            st.session_state["state"] = True
        else:
            st.session_state["message"] = f'Username e/ou senha incorretos, deseja criar uma conta?'
            st.session_state["state"] = False

def register_user(nName, nUsername, nEmail, nPassword, nCartao, nCredit):
    new_user = User(nName, nUsername, nEmail, nPassword, nCartao, nCredit)
    success = controller.create_user(new_user)

    time.sleep(1)
    if success:
        st.session_state["state"] = True

# def openHome():
#         st.session_state["page"] = 'home'

def login_page(self):
    st.title("Login")

    with st.container():
        st.image(
            image = "../assets/perfil.png"
        )

        username = st.text_input(
            label='Username',
            placeholder = "Digite aqui seu username"
        )
        senha = st.text_input(
            label='Senha',
            placeholder = "Digite aqui sua senha"
        )

        botao_login = st.button(
            label="Login",
            help="Fazer login",
            # on_click = self.openHome(),
            kwargs={
                "username": username, 
                "password": senha, 
                "aut": "Login"}
        )

        st.markdown("Não possui conta? Cadastre-se!")
        botao_cadastro = st.button(
            label="Cadastre-se",
            help="Cadastro",
            # on_click = ,
            kwargs={
                "username": username, 
                "passowrd": senha, 
                "aut": "Cadastro"},
            disabled=st.session_state["state"]
        )

    if botao_login:
        st.write("Logando")
        st.session_state["page"] = 'home'

    if botao_cadastro:
        st.session_state["page"] = 'cadastro'

