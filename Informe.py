import streamlit as st
import pandas as pd

# Carrega o arquivo CSV
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

file_path = 'IMDbMovies.csv'
data = load_data(file_path)

# Mostra a quantidade de colunas e linhas
num_columns = len(data.columns)
num_rows = len(data)

st.write(f"Quantidade de colunas: {num_columns}")
st.write(f"Quantidade de linhas: {num_rows}")

# Mostra a tabela
st.write("Tabela de Dados:")
st.write(data)

# Filtro por título
st.sidebar.title('Filtro por Título')
title_filter = st.sidebar.text_input('Digite o título:')
filtered_data = data[data['Title'].str.contains(title_filter, case=False)]

# Mostra os resultados do filtro
st.write(f"Quantidade de resultados para '{title_filter}': {len(filtered_data)}")
st.write(filtered_data)
