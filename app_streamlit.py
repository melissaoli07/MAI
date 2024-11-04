import streamlit as st
import requests

# Título da página Streamlit
st.title("Classificação do Tipo de Comprador")

# Entradas do usuário
quantidade = st.number_input("Quantidade em unidade", min_value=0)
unit_price = st.number_input("Preço unitário", min_value=0.0)
customer_id = st.number_input("ID do Cliente", min_value=0)
month = st.number_input("Mês da Compra", min_value=1, max_value=12)
total_spent = st.number_input("Total gasto", min_value=0.0)
average_price = st.number_input("Preço médio", min_value=0.0)
frequency = st.number_input("Frequência de compra", min_value=0)

# Botão para enviar dados e fazer a previsão
if st.button("Classificar Comprador"):
    # Fazer uma requisição para a API Flask
    url = "http://127.0.0.1:5000/prever"  # URL do seu endpoint Flask
    params = {
        'quantity': quantidade,
        'unitPrice': unit_price,
        'costumerId': customer_id,
        'month': month,
        'totalSpent': total_spent,
        'avaregePrice': average_price,
        'frequency': frequency
    }

    # Chamada da API Flask e tratamento da resposta
    response = requests.get(url, params=params)
    if response.status_code == 200:
        previsao = response.json().get("previsao do grupo de cliente")
        st.success(f"O tipo de comprador é: {previsao}")
    else:
        st.error("Erro na classificação. Verifique a API Flask.")
