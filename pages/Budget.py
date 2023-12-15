import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Remover linhas com valores ausentes na coluna 'Budget'
data = data.dropna(subset=['Budget'])

# Gráfico dos 10 maiores Budgets
st.subheader('Top 10 Maiores Orçamentos')
top_budget = data.nlargest(10, 'Budget')
if not top_budget.empty:
    plt.figure(figsize=(10, 6))
    plt.barh(top_budget['Title'], top_budget['Budget'])
    plt.xlabel('Orçamento')
    plt.title('Top 10 Maiores Orçamentos')
    st.pyplot()
else:
    st.write('Não há dados disponíveis para os 10 maiores orçamentos.')

# Gráfico dos 10 maiores Gross Worldwide
st.subheader('Top 10 Maiores Ganhas Globais')
top_gross = data.nlargest(10, 'Gross worldwide')
if not top_gross.empty:
    plt.figure(figsize=(10, 6))
    plt.barh(top_gross['Title'], top_gross['Gross worldwide'])
    plt.xlabel('Gross Worldwide')
    plt.title('Top 10 Maiores Ganhas Globais')
    st.pyplot()
else:
    st.write('Não há dados disponíveis para os 10 maiores ganhos globais.')

# Gráfico de Budget geral por Release Year
st.subheader('Orçamento Geral por Ano de Lançamento')
budget_by_year = data.groupby('Release Year')['Budget'].sum()
if not budget_by_year.empty:
    plt.figure(figsize=(10, 6))
    budget_by_year.plot(kind='bar')
    plt.xlabel('Ano de Lançamento')
    plt.ylabel('Orçamento Total')
    plt.title('Orçamento Geral por Ano de Lançamento')
    st.pyplot()
else:
    st.write('Não há dados disponíveis para o orçamento geral por ano de lançamento.')
