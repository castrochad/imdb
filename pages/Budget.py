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


# Gráfico dos 10 maiores Ratings
top_rating = data.sort_values('Rating', ascending=False).head(10)
if not top_rating.empty:
    plt.figure(figsize=(10, 6))
    plt.barh(top_rating['Title'], top_rating['Rating'])
    plt.xlabel('Rating')
    plt.title('Top 10 Maiores Ratings')
    img_rating = 'top_10_ratings.png'
    plt.savefig(img_rating, bbox_inches='tight')
    st.image(img_rating)
    plt.close()
else:
    st.write('Não há dados disponíveis para os 10 maiores ratings.')

