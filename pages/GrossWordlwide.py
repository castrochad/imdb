import streamlit as st
import pandas as pd

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Verificar e tratar valores nulos e zeros em 'Budget' e 'Gross worldwide'
data['Budget'] = pd.to_numeric(data['Budget'], errors='coerce')
data['Gross worldwide'] = pd.to_numeric(data['Gross worldwide'], errors='coerce')

# Remover linhas com valores nulos em 'Budget' e 'Gross worldwide'
data = data.dropna(subset=['Budget', 'Gross worldwide'])

# Verificar se existem valores iguais a zero em 'Budget' e 'Gross worldwide'
zero_budget = data['Budget'] == 0
zero_gross = data['Gross worldwide'] == 0

# Exibir contagem de valores nulos, zeros e linhas vazias
st.write(f'Valores nulos em Budget: {data["Budget"].isnull().sum()}')
st.write(f'Valores nulos em Gross worldwide: {data["Gross worldwide"].isnull().sum()}')
st.write(f'Valores zero em Budget: {zero_budget.sum()}')
st.write(f'Valores zero em Gross worldwide: {zero_gross.sum()}')

# Calcular a porcentagem do orçamento em relação ao 'Gross worldwide'
data['pct_do_orcamento'] = (data['Budget'] / data['Gross worldwide']) * 100

# Calcular as porcentagens para 'Gross in US & Canada' e 'Opening Weekend Gross in US & Canada'
data['pct_gross_us_canada'] = (data['Gross in US & Canada'] / data['Gross worldwide']) * 100
data['pct_opening_weekend'] = (data['Opening Weekend Gross in US & Canada'] / data['Gross worldwide']) * 100

# Criar coluna de relação entre Rating e Number of Ratings
data['rating_rel_number_of_ratings'] = data['Rating'] / data['Number of Ratings']

# Exibir as colunas processadas
st.write(data[['Budget', 'Gross worldwide', 'pct_do_orcamento', 'Gross in US & Canada', 'Opening Weekend Gross in US & Canada', 'pct_gross_us_canada', 'pct_opening_weekend', 'Rating', 'Number of Ratings', 'rating_rel_number_of_ratings']])
