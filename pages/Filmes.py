import streamlit as st
import pandas as pd

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Criar lista de títulos
titles = data['Title'].unique().tolist()

# Adicionar um seletor de filmes
selected_movie = st.selectbox('Selecione um filme:', titles)

# Exibir informações do filme selecionado
selected_info = data[data['Title'] == selected_movie]

if not selected_info.empty:
    st.subheader(f'Informações do filme: {selected_movie}')
    st.write('Rating:', selected_info['Rating'].values[0])
    st.write('Motion Picture Rating:', selected_info['Motion Picture Rating'].values[0])
    st.write('Runtime:', selected_info['Runtime'].values[0])
    st.write('Budget:', selected_info['Budget'].values[0])
    st.write('Gross Worldwide:', selected_info['Gross worldwide'].values[0])
    
    gross_worldwide = selected_info['Gross worldwide'].values[0]
    gross_us_canada = selected_info['Gross in US & Canada'].values[0]
    opening_weekend_gross = selected_info['Opening Weekend Gross in US & Canada'].values[0]
    
    st.write(f'Gross worldwide: {gross_worldwide}')
    st.write(f'Gross in US & Canada: {gross_us_canada}')
    st.write(f'Opening Weekend Gross in US & Canada: {opening_weekend_gross}')
else:
    st.write('Nenhuma informação disponível para o filme selecionado.')
