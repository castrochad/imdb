import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega o arquivo CSV
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

file_path = 'IMDbMovies.csv'
data = load_data(file_path)

# Define as opções de filtro
available_columns = [
    'Director', 'Writer', 'Main Genres', 'Motion Picture Rating',
    'Release Year', 'Rating', 'Number of Ratings', 'Budget',
    'Gross in US & Canada', 'Gross worldwide', 'Opening Weekend Gross in US & Canada'
]

# Seleciona a coluna para filtro
selected_column = st.sidebar.selectbox('Selecione a coluna para filtro:', available_columns)

# Filtro por valor na coluna selecionada
filter_value = st.sidebar.text_input(f'Filtrar por {selected_column}:')
filtered_data = data[data[selected_column].str.contains(filter_value, na=False)]

# Exibir estatísticas básicas dos dados filtrados
st.write(f"Estatísticas de '{filter_value}' em '{selected_column}':")
st.write(filtered_data.describe())

# Filtro por valor na coluna selecionada apenas se for uma coluna de texto
if data[selected_column].dtype == 'object':  # Verifica se é uma coluna de texto/string
    filtered_data = data[data[selected_column].str.contains(filter_value, na=False)]
else:
    # Se não for uma coluna de texto, filtra sem usar o método .str.contains()
    filtered_data = data[data[selected_column] == filter_value]

# Exibir estatísticas básicas dos dados filtrados
st.write(f"Estatísticas de '{filter_value}' em '{selected_column}':")
st.write(filtered_data.describe())

# Resto do código para os gráficos e visualizações...

# Gráfico de barras para contagem de filmes por gênero
if selected_column == 'Main Genres':
    genre_counts = filtered_data['Main Genres'].value_counts()
    st.write("Contagem de filmes por gênero:")
    st.bar_chart(genre_counts)

# Gráfico de dispersão para orçamento versus lucro bruto
elif selected_column == 'Budget':
    st.write("Gráfico de dispersão - Orçamento vs Lucro Bruto:")
    sns.set(style="whitegrid")
    scatterplot = sns.scatterplot(x='Budget', y='Gross worldwide', data=filtered_data)
    st.pyplot()

# Gráfico de barras para avaliação por ano de lançamento
elif selected_column == 'Release Year':
    st.write("Gráfico de barras - Avaliação por Ano de Lançamento:")
    average_rating_per_year = filtered_data.groupby('Release Year')['Rating'].mean()
    st.bar_chart(average_rating_per_year)

# Adicione mais condições conforme necessário para outras colunas selecionadas

# Mostra os dados filtrados
st.write("Dados Filtrados:")
st.write(filtered_data)

