import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Remover linhas com valores ausentes na coluna 'Budget' e 'Gross worldwide'
data = data.dropna(subset=['Budget', 'Gross worldwide'])

# Gráfico dos 10 maiores Budgets
top_budget = data.sort_values('Budget', ascending=False).head(10)
if not top_budget.empty:
    plt.figure(figsize=(10, 6))
    plt.barh(top_budget['Title'], top_budget['Budget'])
    plt.xlabel('Orçamento')
    plt.title('Top 10 Maiores Orçamentos')
    img_budget = 'top_10_budgets.png'
    plt.savefig(img_budget, bbox_inches='tight')
    st.image(img_budget)
    plt.close()
else:
    st.write('Não há dados disponíveis para os 10 maiores orçamentos.')

# Gráfico dos 10 maiores Gross Worldwide
top_gross = data.sort_values('Gross worldwide', ascending=False).head(10)
if not top_gross.empty:
    plt.figure(figsize=(10, 6))
    plt.barh(top_gross['Title'], top_gross['Gross worldwide'])
    plt.xlabel('Gross Worldwide')
    plt.title('Top 10 Maiores Ganhas Globais')
    img_gross = 'top_10_gross.png'
    plt.savefig(img_gross, bbox_inches='tight')
    st.image(img_gross)
    plt.close()
else:
    st.write('Não há dados disponíveis para os 10 maiores ganhos globais.')

# Gráfico de Budget geral por Release Year
budget_by_year = data.groupby('Release Year')['Budget'].sum().reset_index()
if not budget_by_year.empty:
    plt.figure(figsize=(10, 6))
    plt.bar(budget_by_year['Release Year'], budget_by_year['Budget'])
    plt.xlabel('Ano de Lançamento')
    plt.ylabel('Orçamento Total')
    plt.title('Orçamento Geral por Ano de Lançamento')
    img_budget_year = 'budget_by_year.png'
    plt.savefig(img_budget_year, bbox_inches='tight')
    st.image(img_budget_year)
    plt.close()
else:
    st.write('Não há dados disponíveis para o orçamento geral por ano de lançamento.')
