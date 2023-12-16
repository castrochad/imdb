import streamlit as st
import pandas as pd

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Verificar se há valores nulos ou zeros em 'Budget' e 'Gross worldwide'
null_budget = data['Budget'].isnull().sum()
null_gross_worldwide = data['Gross worldwide'].isnull().sum()
zero_budget = (data['Budget'] == 0).sum()
zero_gross_worldwide = (data['Gross worldwide'] == 0).sum()

# Tratar os valores nulos ou zeros
if null_budget > 0 or null_gross_worldwide > 0 or zero_budget > 0 or zero_gross_worldwide > 0:
    st.write("Existem valores nulos ou zeros em 'Budget' ou 'Gross worldwide'.")
else:
    # Calcular a porcentagem do orçamento em relação ao 'Gross worldwide'
    data['pct_do_orcamento'] = (data['Budget'] / data['Gross worldwide']) * 100

    # Calcular as porcentagens para 'Gross in US & Canada' e 'Opening Weekend Gross in US & Canada'
    data['pct_gross_us_canada'] = (data['Gross in US & Canada'] / data['Gross worldwide']) * 100
    data['pct_opening_weekend'] = (data['Opening Weekend Gross in US & Canada'] / data['Gross worldwide']) * 100

    # Criar coluna de relação entre Rating e Number of Ratings
    data['rating_rel_number_of_ratings'] = data['Rating'] / data['Number of Ratings']

    # Exibir os dados processados
    st.write(data[['Budget', 'Gross worldwide', 'pct_do_orcamento', 'Gross in US & Canada', 'Opening Weekend Gross in US & Canada', 'pct_gross_us_canada', 'pct_opening_weekend', 'Rating', 'Number of Ratings', 'rating_rel_number_of_ratings']])
