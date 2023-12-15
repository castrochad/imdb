import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Criar lista de títulos
titles = data['Title'].unique().tolist()

# Adicionar um seletor de filmes
selected_movie = st.selectbox('Selecione um filme:', titles)

# Exibir informações do filme selecionado
selected_info = data[data['Title'] == selected_movie]

if not selected_info.empty:
    st.subheader(f'Informações do filme: {selected_movie}')
    st.write('Rating:', selected_info['Rating'].values[0])
    st.write('Motion Picture Rating:', selected_info['Motion Picture Rating'].values[0])
    st.write('Runtime:', selected_info['Runtime'].values[0])
    st.write('Budget:', selected_info['Budget'].values[0])
    st.write('Gross Worldwide:', selected_info['Gross worldwide'].values[0])

    # Cálculo dos percentuais
    gross_values = [
        selected_info['Gross in US & Canada'].values[0],
        selected_info['Opening Weekend Gross in US & Canada'].values[0],
        selected_info['Gross worldwide'].values[0]
    ]
    labels = ['Gross in US & Canada', 'Opening Weekend Gross in US & Canada', 'Gross worldwide']

    if not pd.isnull(gross_values).any():
        fig, ax = plt.subplots()
        ax.pie(gross_values, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12})
        ax.axis('equal')
        st.pyplot(fig)
    else:
        st.write('Há valores ausentes para criar o gráfico de pizza.')
else:
    st.write('Nenhuma informação disponível para o filme selecionado.')
