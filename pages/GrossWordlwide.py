import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Transformar as colunas numéricas necessárias para float
numeric_columns = ['Budget', 'Gross in US & Canada', 'Gross worldwide', 'Opening Weekend Gross in US & Canada']
data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Agrupar os dados por ano e calcular as estatísticas
grouped_data = data.groupby('Release Year').agg({
    'Budget': 'sum',
    'Gross worldwide': 'sum',
    'Gross in US & Canada': 'sum',
    'Opening Weekend Gross in US & Canada': 'sum'
}).reset_index()

# Calcular os percentuais
grouped_data['Pct_Budget_to_Worldwide'] = (grouped_data['Budget'] / grouped_data['Gross worldwide']) * 100
grouped_data['Pct_USCanada_to_Worldwide'] = (grouped_data['Gross in US & Canada'] / grouped_data['Gross worldwide']) * 100
grouped_data['Pct_OpeningWeekend_to_Worldwide'] = (grouped_data['Opening Weekend Gross in US & Canada'] / grouped_data['Gross worldwide']) * 100

# Exibir o seletor de ano
selected_year = st.selectbox('Selecione um ano:', grouped_data['Release Year'])

# Filtrar os dados para o ano selecionado
selected_info = grouped_data[grouped_data['Release Year'] == selected_year]

# Exibir as informações se houver dados para o ano selecionado
if not selected_info.empty:
    st.write(f'Informações para o ano {selected_year}:')
    st.write(selected_info)

    # Criar um gráfico para exibir os percentuais
    plt.figure(figsize=(10, 6))
    plt.bar(selected_info.columns[4:], selected_info.values[0][4:], color=['blue', 'orange', 'green'])
    plt.xlabel('Tipos de percentuais')
    plt.ylabel('Valores em %')
    plt.title(f'Percentuais para o ano {selected_year}')
    st.pyplot(plt)

else:
    st.write('Nenhuma informação disponível para o ano selecionado.')
