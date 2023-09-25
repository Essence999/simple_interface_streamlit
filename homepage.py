import streamlit as st
import pandas as pd

st.set_page_config(page_title='Dados de ISSTH', layout='wide', page_icon='o')

with st.container():
    st.subheader('Site com o Streamlit')
    st.title('Dashboard de I Shall Seal the Heavens')
    st.write('Informações sobre a obra')
    st.write(
        'Teste de link: [github](https://github.com/Essence999)')


@st.cache_data
def carregar_dados():
    tabela = pd.read_csv('issth.csv')
    return tabela


with st.container():
    lista_de_range = ['1-100', '101-200', '201-300', '301-400', '1600-1614']
    qtde_title = st.selectbox('Selecione o número de títulos', lista_de_range)
    numeros = qtde_title.split('-')
    num = [int(num) for num in numeros]
    dados = carregar_dados()
    dados = dados[num[0]:num[1]]
    st.area_chart(dados, x='title', y='characters')
