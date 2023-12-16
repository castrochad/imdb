import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Adicionar um seletor de colunas para o usuário
selected_columns = st.multiselect('Selecione as colunas:', data.columns)

# Adicionar um seletor de ano
selected_year = st.slider('Selecione um ano:', int(data['Release Year'].min()), int(data['Release Year'].max()))

if selected_columns:
    # Filtrar os dados para o ano selecionado
    filtered_data = data[data['Release Year'] == selected_year]

    # Garantir que apenas as colunas numéricas sejam selecionadas
    numeric_columns = filtered_data.select_dtypes(include='number').columns.tolist()

    # Verificar se as colunas selecionadas são numéricas
    selected_numeric_columns = list(set(selected_columns).intersection(set(numeric_columns)))

    if selected_numeric_columns:
        # Agrupar os dados por ano e calcular as estatísticas
        grouped_data = filtered_data.groupby('Release Year')[selected_numeric_columns].sum().reset_index()

        # Calcular os percentuais para cada coluna selecionada
        for col in selected_numeric_columns:
            grouped_data[f'Pct_{col}_to_Worldwide'] = (grouped_data[col] / grouped_data[col].sum()) * 100

        # Exibir os gráficos
        st.write(f'Gráficos percentuais para o ano {selected_year}:')

        for col in selected_numeric_columns:
            plt.figure(figsize=(8, 6))
            plt.bar(grouped_data['Release Year'], grouped_data[f'Pct_{col}_to_Worldwide'], color='skyblue')
            plt.xlabel('Ano de lançamento')
            plt.ylabel(f'Percentual em relação ao total de {col}')
            plt.title(f'Percentual de {col} por ano de lançamento')
            st.pyplot(plt)

    else:
        st.write('Nenhuma coluna numérica foi selecionada!')

else:
    st.write('Nenhuma coluna foi selecionada!')
