import streamlit as st
import pandas as pd

# Carregar os dados
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

file_path = 'IMDbMovies.csv'
data = load_data(file_path)

# Filtro por Release Year
selected_year = st.sidebar.selectbox('Selecione o ano de lançamento:', data['Release Year'].unique())
filtered_by_year = data[data['Release Year'] == selected_year]

# Filtrar por Runtime
runtime_1h = filtered_by_year[filtered_by_year['Runtime'] < '2h']
runtime_2h = filtered_by_year[(filtered_by_year['Runtime'] >= '2h') & (filtered_by_year['Runtime'] < '3h')]
runtime_3h = filtered_by_year[filtered_by_year['Runtime'] >= '3h']

# Exibir os resultados
st.write(f"Filmes lançados no ano de {selected_year}:")
st.write(filtered_by_year)

st.write("Filmes com menos de 2 horas de duração:")
st.write(runtime_1h)

st.write("Filmes com duração entre 2 e 3 horas:")
st.write(runtime_2h)

st.write("Filmes com mais de 3 horas de duração:")
st.write(runtime_3h)
