import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

file_path = 'IMDbMovies.csv'
data = load_data(file_path)

# Top 10 filmes mais caros (budget) analisando o lucro e valor arrecadado na semana de estreia
top_10_budget = data.nlargest(10, 'Budget')
st.subheader('Top 10 Filmes Mais Caros (Budget)')
st.write(top_10_budget)

# Gráfico - Orçamento em filmes ao passar dos anos
st.subheader('Orçamento dos Filmes ao Longo dos Anos')
budget_over_years = data.groupby('Release Year')['Budget'].sum()
st.line_chart(budget_over_years)

# Top 10 filmes de maior bilheteria (gross worldwide) analisando a percentagem no US|Canada e Open Weekend
top_10_gross = data.nlargest(10, 'Gross worldwide')
top_10_gross['pct_US_Canada'] = top_10_gross['Gross in US & Canada'] / top_10_gross['Gross worldwide']
top_10_gross['pct_Open_Weekend'] = top_10_gross['Opening Weekend Gross in US & Canada'] / top_10_gross['Gross worldwide']
st.subheader('Top 10 Filmes de Maior Bilheteria')
st.write(top_10_gross)

# Gráfico - Motion Picture Rating por número de votos
st.subheader('Motion Picture Rating por Número de Votos')
sns.scatterplot(x='Motion Picture Rating', y='Number of Ratings', data=data)
st.pyplot()
