import pandas as pd

# Carregar os dados
file_path = 'IMDbMovies.csv'
data = pd.read_csv(file_path)

# Criar a coluna 'pct_do_orcamento'
data['pct_do_orcamento'] = data['Gross worldwide'] / data['Budget']

# Criar a coluna 'pct_valor_US'
data['pct_valor_US'] = data['Gross in US & Canada'] / data['Gross worldwide']

# Criar a coluna 'pct_valor_Open_Weekend'
data['pct_valor_Open_Weekend'] = data['Opening Weekend Gross in US & Canada'] / data['Gross worldwide']

# Criar a coluna 'relacao_rating_votos'
data['relacao_rating_votos'] = data['Rating'] * data['Number of Ratings']

# Exibir as primeiras linhas com as novas colunas
print(data.head())
