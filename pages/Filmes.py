import streamlit as st
import pandas as pd

# Carregar os dados
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

file_path = 'IMDbMovies.csv'
data = load_data(file_path)

# Filtrar por Release Year
selected_year = st.sidebar.selectbox('Selecione o ano de lançamento:', data['Release Year'].unique())
filtered_by_year = data[data['Release Year'] == selected_year]

# Filtrar por Runtime
runtime_1h = filtered_by_year[filtered_by_year['Runtime'] == '1h']
runtime_2h = filtered_by_year[filtered_by_year['Runtime'] == '2h']
runtime_3h = filtered_by_year[filtered_by_year['Runtime'] == '3h']

# Exibir os resultados
st.write(f"Filmes lançados no ano de {selected_year}:")
st.write(filtered_by_year)

st.write("Filmes com duração de 1h:")
st.write(runtime_1h)

st.write("Filmes com duração de 2h:")
st.write(runtime_2h)

st.write("Filmes com duração de 3h:")
st.write(runtime_3h)
