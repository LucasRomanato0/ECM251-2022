from cProfile import label
from faulthandler import disable
from tkinter import DISABLED
from tkinter.ttk import Style
import streamlit as st

st.title('Carrinho:')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Prod1", "Prod2", "Prod3", "Prod4", "Total $"])

valor1 = 5623.87
valor2 = 2.90
valor3 = 198.43
valor4 = 0.42

qtd1 = 1
qtd2 = 10
qtd3 = 2
qtd4 = 36

with tab1:
       total1 = valor1*qtd1

       st.header("Produto 1")
       st.image(
            image = '../assets/produto.png'
       )
       st.subheader(f"Quantidade: {qtd1}")
       # st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
       st.text(f"Valor por unidade: R${valor1}")
       st.caption(f"Total: R${total1:,.2f}")
       st.button(
              label = "Mais detalhes do produto1",
       )

with tab2:
       total2 = valor2*qtd2
       
       st.header("Produto 2")
       st.image(
            image = '../assets/produto.png'
       )
       st.subheader(f"Quantidade: {qtd2}")
       # st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
       st.text(f"Valor por unidade: R${valor2}")
       st.caption(f"Total: R${total2:,.2f}")
       st.button(
              label = "Mais detalhes do produto2",
       )

with tab3:
       total3 = valor3*qtd3

       st.header("Produto 3")
       st.image(
            image = '../assets/produto.png'
       )
       st.subheader(f"Quantidade: {qtd3}")
       # st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
       st.text(f"Valor por unidade: R${valor3}")
       st.caption(f"Total: R${total3:,.2f}")
       st.button(
              label = "Mais detalhes do produto3",
       )

with tab4:
       total4 = valor4*qtd4

       st.header("Produto 4")
       st.image(
            image = '../assets/produto.png'
       )
       st.subheader(f"Quantidade: {qtd4}")
       # st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
       st.text(f"Valor por unidade: R${valor4}")
       st.caption(f"Total: R${total4:,.2f}")
       st.button(
              label = "Mais detalhes do produto4",
       )

with tab5:
       total = total1 + total2 + total3 + total4
       st.header(f"Total a pagar: {total:,.2f}")
       st.button(
              label = "Pagar"
       )