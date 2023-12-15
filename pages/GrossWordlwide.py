import streamlit as st
import pandas as pd

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Verificar e substituir valores infinitos ou NaN por zeros
data = data.replace([float('inf'), -float('inf')], float('nan'))
data = data.fillna(0)

# Calcular as colunas percentuais
data['pct_do_orcamento'] = data['Gross worldwide'] / data['Budget']
data['pct_valor_US'] = data['Gross in US & Canada'] / data['Gross worldwide']
data['pct_valor_Open_Weekend'] = data['Opening Weekend Gross in US & Canada'] / data['Gross worldwide']

# Exibir os dados e gráficos
st.write("Dados com colunas percentuais:")
st.write(data.head())

# Gráfico de barras para pct_do_orcamento
st.write("Gráfico de pct_do_orcamento:")
bar_chart_budget = data['pct_do_orcamento'].plot(kind='bar')
st.pyplot(bar_chart_budget)

# Gráfico de barras para pct_valor_US e pct_valor_Open_Weekend
st.write("Gráfico de pct_valor_US e pct_valor_Open_Weekend:")
bar_chart_values = data[['pct_valor_US', 'pct_valor_Open_Weekend']].plot(kind='bar', stacked=True)
st.pyplot(bar_chart_values)
