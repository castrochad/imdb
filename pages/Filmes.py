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

# Aplica a filtragem
if filter_value:  # Verifica se há algum valor no campo de filtro
    filtered_data = data[data[selected_column].astype(str).str.contains(filter_value, na=False)]
    
    # Exibir estatísticas básicas dos dados filtrados
    st.write(f"Estatísticas de '{filter_value}' em '{selected_column}':")
    st.write(filtered_data.describe())

    # Resto do código para os gráficos e visualizações...
    if selected_column == 'Main Genres':
        genre_counts = filtered_data['Main Genres'].value_counts()
        st.write("Contagem de filmes por gênero:")
        st.bar_chart(genre_counts)

    elif selected_column == 'Budget':
        st.write("Gráfico de dispersão - Orçamento vs Lucro Bruto:")
        sns.set(style="whitegrid")
        scatterplot = sns.scatterplot(x='Budget', y='Gross worldwide', data=filtered_data)
        st.pyplot()

    elif selected_column == 'Release Year':
        st.write("Gráfico de barras - Avaliação por Ano de Lançamento:")
        average_rating_per_year = filtered_data.groupby('Release Year')['Rating'].mean()
        st.bar_chart(average_rating_per_year)

    # Adicione mais condições conforme necessário para outras colunas selecionadas

    # Mostra os dados filtrados
    st.write("Dados Filtrados:")
    st.write(filtered_data)
else:
    # Se não houver valor de filtro, exibe apenas os dados originais
    st.write("Dados Originais:")
    st.write(data)
