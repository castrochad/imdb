import streamlit as st
import pandas as pd
import re

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
    
    gross_worldwide = selected_info['Gross worldwide'].values[0]
    gross_us_canada = selected_info['Gross in US & Canada'].values[0]
    opening_weekend_gross = selected_info['Opening Weekend Gross in US & Canada'].values[0]
    
    # Função para remover caracteres não numéricos e converter para float
    def clean_and_convert(value):
        cleaned_value = re.sub(r'[^\d.]', '', value)  # Remove tudo exceto dígitos e pontos
        try:
            return float(cleaned_value)
        except ValueError:
            return None  # Em caso de erro na conversão
    
    gross_worldwide = clean_and_convert(gross_worldwide)
    gross_us_canada = clean_and_convert(gross_us_canada)
    opening_weekend_gross = clean_and_convert(opening_weekend_gross)
    
    st.write(f'Gross worldwide: {gross_worldwide}')
    st.write(f'Gross in US & Canada: {gross_us_canada}')
    st.write(f'Opening Weekend Gross: {opening_weekend_gross}')
    
    # Calcular percentuais
    if gross_worldwide:
        percentage_gross_us_canada = (gross_us_canada / gross_worldwide) * 100
        percentage_opening_weekend = (opening_weekend_gross / gross_worldwide) * 100
        
        st.write(f'Percentage of Gross in US & Canada: {percentage_gross_us_canada:.2f}%')
        st.write(f'Percentage of Opening Weekend Gross: {percentage_opening_weekend:.2f}%')
    else:
        st.write('Não é possível calcular os percentuais.')
else:
    st.write('Nenhuma informação disponível para o filme selecionado.')
