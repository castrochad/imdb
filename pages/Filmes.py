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

    # Verificar se as colunas necessárias para o gráfico estão presentes
    if 'Gross worldwide' in selected_info.columns and 'Gross in US & Canada' in selected_info.columns and 'Opening Weekend Gross in US & Canada' in selected_info.columns:
        gross_values = selected_info[['Gross worldwide', 'Gross in US & Canada', 'Opening Weekend Gross in US & Canada']].values[0]
        labels = ['Gross worldwide', 'Gross in US & Canada', 'Opening Weekend Gross']

        # Verificar se há valores nulos
        if not pd.isnull(gross_values).any():
            fig, ax = plt.subplots()
            ax.pie(gross_values, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig)
        else:
            st.write('Há valores ausentes para criar o gráfico de pizza.')
    else:
        st.write('As colunas necessárias para criar o gráfico não estão presentes no conjunto de dados.')
else:
    st.write('Nenhuma informação disponível para o filme selecionado.')
