import streamlit as st

st.title("Pagamento")

col1, col2 = st.columns(2)

with st.container():
    st.header("Nome do produto")
    pagamento = st.selectbox(
        "Escolha a forma de pagamento",
        ('Cartão Débito', 'Cartão Crédito', 'Pix', 'Boleto', 'PicPay')
    )
    if(pagamento == 'Boleto'):
        st.write('Gerar Boleto')
    else:
        st.write('Prosseguir pagamento com', pagamento)


with col1:
    st.image(
        image = '../assets/produto.png',
        width = 250
    )

with col2:
    st.text("Detalhes do pagamento")