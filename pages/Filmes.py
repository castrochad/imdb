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
    
    gross_worldwide = float(selected_info['Gross worldwide'].values[0])
    gross_us_canada = float(selected_info['Gross in US & Canada'].values[0])
    opening_weekend_gross = float(selected_info['Opening Weekend Gross in US & Canada'].values[0])
    
    # Cálculo dos percentuais
    percent_gross_us_canada = (gross_us_canada / gross_worldwide) * 100
    percent_opening_weekend = (opening_weekend_gross / gross_worldwide) * 100
    
    st.write(f'Percentual de Gross in US & Canada em relação ao Gross Worldwide: {percent_gross_us_canada:.2f}%')
    st.write(f'Percentual de Opening Weekend Gross em relação ao Gross Worldwide: {percent_opening_weekend:.2f}%')
else:
    st.write('Nenhuma informação disponível para o filme selecionado.')
