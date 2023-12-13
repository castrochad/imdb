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

# Obter as colunas de dados inteiros e categóricos
integer_columns = data.select_dtypes(include='int64').columns.tolist()
string_columns = data.select_dtypes(include='object').columns.tolist()

# Sidebar para selecionar o tipo de gráfico e a coluna
chart_type = st.sidebar.selectbox('Selecione o tipo de gráfico:', ['Barra', 'Dispersão'])
selected_column = st.sidebar.selectbox('Selecione a coluna:', string_columns + integer_columns)

# Filtro por valor na coluna selecionada
filter_value = st.sidebar.text_input(f'Filtrar por {selected_column}:')

# Aplicar filtro
filtered_data = data
if filter_value:
    filtered_data = data[data[selected_column].astype(str).str.contains(filter_value, na=False)]

# Exibir gráficos baseados no tipo selecionado
st.title(f'Gráfico de {chart_type} para {selected_column}')
if chart_type == 'Barra':
    if selected_column in string_columns:
        values_count = filtered_data[selected_column].value_counts()
        st.bar_chart(values_count)
    elif selected_column in integer_columns:
        st.warning('Selecione uma coluna categórica para o gráfico de barras.')
elif chart_type == 'Dispersão':
    if selected_column in integer_columns:
        x_axis = st.selectbox('Selecione a coluna para o eixo x:', integer_columns)
        scatterplot = sns.scatterplot(x=x_axis, y=selected_column, data=filtered_data)
        st.pyplot()
    else:
        st.warning('Selecione uma coluna numérica para o gráfico de dispersão.')
