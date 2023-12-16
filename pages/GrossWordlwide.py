import streamlit as st
import pandas as pd

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Adicionar um seletor de filmes
titles = data['Title'].unique().tolist()
selected_movie = st.selectbox('Selecione um filme:', titles)

# Filtrar os dados com base no filme selecionado
selected_info = data[data['Title'] == selected_movie]

if not selected_info.empty:
    # Calcular e exibir as informações
    budget = selected_info['Budget'].values[0]
    gross_worldwide = selected_info['Gross worldwide'].values[0]
    gross_us_canada = selected_info['Gross in US & Canada'].values[0]
    opening_weekend_us_canada = selected_info['Opening Weekend Gross in US & Canada'].values[0]
    rating = selected_info['Rating'].values[0]
    num_ratings = selected_info['Number of Ratings'].values[0]

    st.write(f'Informações do filme: {selected_movie}')
    st.write(f'Budget: {budget}')
    st.write(f'Gross worldwide: {gross_worldwide}')
    st.write(f'Pct_do_orcamento: {budget / gross_worldwide * 100:.2f}%')
    st.write(f'Gross in US & Canada: {gross_us_canada}')
    st.write(f'Opening Weekend Gross in US & Canada: {opening_weekend_us_canada}')
    st.write(f'Pct_gross_us_canada: {gross_us_canada / gross_worldwide * 100:.2f}%')
    st.write(f'Pct_opening_weekend: {opening_weekend_us_canada / gross_worldwide * 100:.2f}%')
    st.write(f'Rating: {rating}')
    st.write(f'Number of Ratings: {num_ratings}')
    st.write(f'Rating_rel_number_of_ratings: {rating / num_ratings:.2f}')

else:
    st.write('Nenhuma informação disponível para o filme selecionado.')
