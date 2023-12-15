import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Remover linhas onde 'Budget' ou 'Gross worldwide' são nulos para evitar erros
data = data.dropna(subset=['Budget', 'Gross worldwide'])

# Gráfico dos maiores Budgets
st.subheader("Top 10 Maiores Budgets")
top_budget = data.nlargest(10, 'Budget')
plt.figure(figsize=(10, 6))
plt.barh(top_budget['Title'], top_budget['Budget'])
plt.xlabel('Budget')
plt.title('Top 10 Maiores Budgets')
st.pyplot()

# Gráfico dos maiores Gross Worldwide
st.subheader("Top 10 Maiores Gross Worldwide")
top_gross = data.nlargest(10, 'Gross worldwide')
plt.figure(figsize=(10, 6))
plt.barh(top_gross['Title'], top_gross['Gross worldwide'])
plt.xlabel('Gross Worldwide')
plt.title('Top 10 Maiores Gross Worldwide')
st.pyplot()

# Gráfico de orçamento ao passar dos anos
st.subheader("Orçamento ao Passar dos Anos")
budget_over_years = data.groupby('Release Year')['Budget'].sum().reset_index()
budget_over_years['Release Year'] = budget_over_years['Release Year'].astype(str)
plt.figure(figsize=(10, 6))
plt.plot(budget_over_years['Release Year'], budget_over_years['Budget'], marker='o')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Orçamento Total')
plt.title('Orçamento ao Passar dos Anos')
st.pyplot()

# Gráfico dos maiores Motion Picture Rating
st.subheader("Top 10 Maiores Motion Picture Rating")
top_rating = data.nlargest(10, 'Motion Picture Rating')
plt.figure(figsize=(10, 6))
plt.barh(top_rating['Title'], top_rating['Motion Picture Rating'])
plt.xlabel('Motion Picture Rating')
plt.title('Top 10 Maiores Motion Picture Rating')
st.pyplot()
