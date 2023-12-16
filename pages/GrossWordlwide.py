import streamlit as st
import pandas as pd

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Remover linhas com valores ausentes em 'Gross worldwide' e 'Budget'
data = data.dropna(subset=['Gross worldwide', 'Budget'])

# Verificar se os valores são números antes de realizar a operação
data['pct_do_orcamento'] = data['Gross worldwide'] / data['Budget'].replace(0, pd.NA)

# Calcular percentuais para 'Gross in US & Canada' e 'Opening Weekend Gross in US & Canada'
data['pct_gross_us_canada'] = data['Gross in US & Canada'] / data['Gross worldwide'].replace(0, pd.NA)
data['pct_opening_weekend'] = data['Opening Weekend Gross in US & Canada'] / data['Gross worldwide'].replace(0, pd.NA)

# Exibir os dados processados
st.write(data[['Gross worldwide', 'Budget', 'pct_do_orcamento', 'Gross in US & Canada', 'Opening Weekend Gross in US & Canada', 'pct_gross_us_canada', 'pct_opening_weekend']])
