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
        grouped_data = filtered_data.groupby('Release Year')[selected_numeric_columns].sum()

        # Calcular os percentuais para cada coluna selecionada
        pct_columns = []
        for col in selected_numeric_columns:
            pct_col_name = f'Pct_{col}_to_Worldwide'
            grouped_data[pct_col_name] = (grouped_data[col] / grouped_data[col].sum()) * 100
            pct_columns.append(pct_col_name)

        # Reiniciar o índice
        grouped_data.reset_index(inplace=True)

        # Exibir os gráficos
        st.write(f'Gráficos percentuais para o ano {selected_year}:')

        for col in pct_columns:
            plt.figure(figsize=(8, 6))
            plt.bar(grouped_data['Release Year'], grouped_data[col], color='skyblue')
            plt.xlabel('Ano de lançamento')
            plt.ylabel(f'Percentual em relação ao total')
            plt.title(f'Percentual por ano de lançamento - {col[4:-13]}')
            st.pyplot(plt)

    else:
        st.write('Nenhuma coluna numérica foi selecionada!')

else:
    st.write('Nenhuma coluna foi selecionada!')
