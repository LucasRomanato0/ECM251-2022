import streamlit as st
from src.views.login import register_user

def cadastro_page():
       new_name = st.text_input('Nome')
       new_email = st.text_input('E-mail')
       new_user = st.text_input('Username')
       new_password = st.text_input('Nova Senha')
       new_cartao = st.text_input('Novo Cartão de Crédito')
       new_credit = st.text_input('Novo Crédito de Conta', 0.0)
       botao_entrar = st.button(
              label="Entrar", 
              help="Finalizar Cadastro",
              on_click=register_user(new_name, new_user, new_email, new_password, new_cartao, new_credit),
              kwargs={
                  "new_name":new_name, 
                  "new_email":new_email, 
                  "new_user":new_user, 
                  "new_password":new_password}
       )