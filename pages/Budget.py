import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Gráfico dos maiores Budgets
st.subheader("Top 10 Maiores Budgets")
top_budget = data.sort_values('Budget', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_budget['Title'], top_budget['Budget'])
plt.xlabel('Budget')
plt.title('Top 10 Maiores Budgets')
st.pyplot()

# Gráfico dos maiores Gross Worldwide
st.subheader("Top 10 Maiores Gross Worldwide")
top_gross = data.sort_values('Gross worldwide', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_gross['Title'], top_gross['Gross worldwide'])
plt.xlabel('Gross Worldwide')
plt.title('Top 10 Maiores Gross Worldwide')
st.pyplot()

# Gráfico de orçamento ao passar dos anos
st.subheader("Orçamento ao Passar dos Anos")
budget_over_years = data.groupby('Release Year')['Budget'].sum()
plt.figure(figsize=(10, 6))
plt.plot(budget_over_years, marker='o')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Orçamento Total')
plt.title('Orçamento ao Passar dos Anos')
st.pyplot()

# Gráfico dos maiores Motion Picture Rating
st.subheader("Top 10 Maiores Motion Picture Rating")
top_rating = data.sort_values('Motion Picture Rating', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_rating['Title'], top_rating['Motion Picture Rating'])
plt.xlabel('Motion Picture Rating')
plt.title('Top 10 Maiores Motion Picture Rating')
st.pyplot()
