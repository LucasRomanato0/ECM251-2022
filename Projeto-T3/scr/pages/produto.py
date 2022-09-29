from cProfile import label
from cgitb import text
from turtle import width
import streamlit as st

col1, col2 = st.columns(2)

with col1:
       st.image(
              image = '../assets/produto.png',
              width = 250
       )

with st.container():
       with col2:
              st.header("Nome do produto")
              st.text("Lorem ipsum dolor sit amet, \nconsectetur adipiscing elit, \nsed do eiusmod tempor incididunt ut \nlabore et dolore magna aliqua. Ut enim ad \nminim veniam, quis nostrud exercitation \nullamco laboris nisi ut aliquip ex ea \ncommodo consequat. Duis aute irure dolor \nin reprehenderit in voluptate velit esse \ncillum dolore eu fugiat nulla pariatur. \nExcepteur sint occaecat cupidatat non \nproident, sunt in culpa qui officia \ndeserunt mollit anim id est laborum.")
              st.button(
                     label = "Adicionar ao carrinho"
              )
              st.button(
                     label = "Calcular frete"
              )