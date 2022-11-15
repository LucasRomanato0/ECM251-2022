from cProfile import label
import streamlit as st

st.title('Produtos:')

prod1, prod2, prod3, prod4 = st.columns(4)

def home_page():
    with st.container():    
        with prod1:
            st.image(
                image = '../assets/produto.png'
            )
            st.text('Valor: R$5623,87')
            st.button(
                label="Produto 1"
            )

        with prod2:
            st.image(
                image = '../assets/produto.png'
            )
            st.text('Valor: R$2,90')
            st.button(
                label="Produto 2"
            )

        with prod3:
            st.image(
                image = '../assets/produto.png'
            )
            st.text('Valor: R$198,43')
            st.button(
                label="Produto 3"
            )

        with prod4:
            st.image(
                image = '../assets/produto.png'
            )
            st.text('Valor: R$0,42')
            st.button(
                label="Produto 4"
            )
