import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Converter colunas para numérico
data['Budget'] = pd.to_numeric(data['Budget'], errors='coerce')
data['Gross worldwide'] = pd.to_numeric(data['Gross worldwide'], errors='coerce')

# Remover linhas com valores nulos
data = data.dropna(subset=['Budget', 'Gross worldwide'])

# Preparar os dados para gráfico dos maiores budgets
top_budget = data.nlargest(10, 'Budget')
plt.figure(figsize=(10, 6))
plt.barh(top_budget['Title'], top_budget['Budget'])
plt.xlabel('Budget')
plt.title('Top 10 Maiores Budgets')
st.pyplot(plt)

# Gráfico dos maiores Gross Worldwide
top_gross = data.nlargest(10, 'Gross worldwide')
plt.figure(figsize=(10, 6))
plt.barh(top_gross['Title'], top_gross['Gross worldwide'])
plt.xlabel('Gross Worldwide')
plt.title('Top 10 Maiores Gross Worldwide')
st.pyplot(plt)

# Gráfico de orçamento ao passar dos anos
budget_over_years = data.groupby('Release Year')['Budget'].sum()
plt.figure(figsize=(10, 6))
plt.plot(budget_over_years, marker='o')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Orçamento Total')
plt.title('Orçamento ao Passar dos Anos')
st.pyplot(plt)

# Gráfico dos maiores Motion Picture Rating
top_rating = data.nlargest(10, 'Motion Picture Rating')
plt.figure(figsize=(10, 6))
plt.barh(top_rating['Title'], top_rating['Motion Picture Rating'])
plt.xlabel('Motion Picture Rating')
plt.title('Top 10 Maiores Motion Picture Rating')
st.pyplot(plt)
