import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

file_path = 'IMDbMovies.csv'
data = load_data(file_path)

# Ordenar os dados pelos Ratings em ordem decrescente
sorted_data = data.sort_values(by='Rating', ascending=False)

# Selecionar os top 10 Ratings
top_10_ratings = sorted_data.head(10)

# Gráfico de barras para os top 10 Ratings
plt.figure(figsize=(10, 6))
sns.barplot(x='Rating', y='Title', data=top_10_ratings, palette='viridis')
plt.title('Top 10 Ratings')
plt.xlabel('Rating')
plt.ylabel('Título do Filme')
plt.xticks(rotation=45)
plt.tight_layout()

# Exibir o gráfico usando Streamlit
st.pyplot(plt)
