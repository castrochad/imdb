import streamlit as st
import pandas as pd

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Criar coluna pct_do_orcamento (Gross Worldwide / Budget)
data['pct_do_orcamento'] = data['Gross worldwide'] / data['Budget']

# Calcular os percentuais para Gross in US & Canada e Opening Weekend Gross in US & Canada
data['pct_Gross_in_US'] = data['Gross in US & Canada'] / data['Gross worldwide']
data['pct_Opening_Weekend'] = data['Opening Weekend Gross in US & Canada'] / data['Gross worldwide']

# Adicionar um seletor de filmes
selected_movie = st.selectbox('Selecione um filme:', data['Title'])

# Exibir informações do filme selecionado
selected_info = data[data['Title'] == selected_movie]

if not selected_info.empty:
    st.subheader(f'Informações do filme: {selected_movie}')
    st.write('Rating:', selected_info['Rating'].values[0])
    st.write('Motion Picture Rating:', selected_info['Motion Picture Rating'].values[0])
    st.write('Runtime:', selected_info['Runtime'].values[0])
    st.write('Budget:', selected_info['Budget'].values[0])
    st.write('Gross Worldwide:', selected_info['Gross worldwide'].values[0])
    st.write('Percentual do Orçamento:', selected_info['pct_do_orcamento'].values[0])
    st.write('Percentual de Gross in US & Canada:', selected_info['pct_Gross_in_US'].values[0])
    st.write('Percentual de Opening Weekend Gross:', selected_info['pct_Opening_Weekend'].values[0])
else:
    st.write('Nenhuma informação disponível para o filme selecionado.')
