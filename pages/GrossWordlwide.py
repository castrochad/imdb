import streamlit as st
import pandas as pd

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Remover linhas com valores ausentes em 'Gross worldwide' e 'Budget'
data = data.dropna(subset=['Gross worldwide', 'Budget'])

# Verificar se os valores são números antes de realizar a operação
data['pct_do_orcamento'] = data.apply(lambda row: row['Gross worldwide'] / row['Budget'] if pd.to_numeric(row['Budget'], errors='coerce') != 0 else 0, axis=1)

# Calcular percentuais para 'Gross in US & Canada' e 'Opening Weekend Gross in US & Canada'
data['pct_gross_us_canada'] = data.apply(lambda row: row['Gross in US & Canada'] / row['Gross worldwide'] if row['Gross worldwide'] != 0 else 0, axis=1)
data['pct_opening_weekend'] = data.apply(lambda row: row['Opening Weekend Gross in US & Canada'] / row['Gross worldwide'] if row['Gross worldwide'] != 0 else 0, axis=1)

# Exibir os dados processados
st.write(data[['Gross worldwide', 'Budget', 'pct_do_orcamento', 'Gross in US & Canada', 'Opening Weekend Gross in US & Canada', 'pct_gross_us_canada', 'pct_opening_weekend']])
