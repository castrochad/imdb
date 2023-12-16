import streamlit as st
import pandas as pd
import numpy as np

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Remover linhas com valores ausentes em 'Gross worldwide' e 'Budget'
data = data.dropna(subset=['Gross worldwide', 'Budget'])

# Calcular a porcentagem do orçamento em relação ao 'Gross worldwide'
data['pct_do_orcamento'] = np.where(data['Budget'] != 0, data['Gross worldwide'] / data['Budget'], 0)

# Calcular as porcentagens para 'Gross in US & Canada' e 'Opening Weekend Gross in US & Canada'
data['pct_gross_us_canada'] = np.where(data['Gross worldwide'] != 0, data['Gross in US & Canada'] / data['Gross worldwide'], 0)
data['pct_opening_weekend'] = np.where(data['Gross worldwide'] != 0, data['Opening Weekend Gross in US & Canada'] / data['Gross worldwide'], 0)

# Exibir os dados processados
st.write(data[['Gross worldwide', 'Budget', 'pct_do_orcamento', 'Gross in US & Canada', 'Opening Weekend Gross in US & Canada', 'pct_gross_us_canada', 'pct_opening_weekend']])
