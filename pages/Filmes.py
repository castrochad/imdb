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

# Filtro por valores não nulos na coluna 'Rating' e 'Release Year'
filtered_data = data[(data['Rating'].notnull()) & (data['Release Year'].notnull())]

# Converter a coluna 'Release Year' para o tipo inteiro (caso não esteja)
filtered_data['Release Year'] = filtered_data['Release Year'].astype(int)

# Converter a coluna 'Rating' para numérico
filtered_data['Rating'] = pd.to_numeric(filtered_data['Rating'], errors='coerce')

# Remover linhas com valores nulos na coluna 'Rating' após a conversão
filtered_data = filtered_data.dropna(subset=['Rating'])

# Agrupar por 'Release Year' e calcular a média dos Ratings
ratings_by_year = filtered_data.groupby('Release Year')['Rating'].mean().reset_index()

# Configurações do gráfico
plt.figure(figsize=(10, 6))
sns.lineplot(x='Release Year', y='Rating', data=ratings_by_year)
plt.title('Média de Rating dos Filmes ao Longo dos Anos')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Rating Médio')
plt.grid(True)

# Exibir o gráfico usando o Streamlit
st.pyplot(plt)
