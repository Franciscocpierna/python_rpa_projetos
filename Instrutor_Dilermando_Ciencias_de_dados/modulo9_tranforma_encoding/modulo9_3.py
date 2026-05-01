## Transformação e Codificação de Variáveis...
## Mini-Projeto 10 - One Hot Encoding


# Para este projeto 10, vamos utilizar novamente o dataset "Mercedes-Benz Greener Manufacturing" utilizado em 
# uma competição do site Kaggle. Você pode ter acesso ao desafio completo e o dataset pelo seguinte endereço: 
# https://www.kaggle.com/c/mercedes-benz-greener-manufacturing

# Ao realizar o processo de "One-Hot Encoding", estamos transformando variáveis categóricas em uma 
# representação binária, onde cada categoria se torna uma coluna binária (0 ou 1). Isso é feito para 
# permitir que algoritmos de aprendizado de máquina possam trabalhar com dados categóricos, já que a maioria 
# dos algoritmos requer entrada numérica.

# Carregando os Pacotes (Dupla dinâmica)
import pandas as pd
import numpy as np

# Vamos definir ou configurar para que consigamos visualizar todas as colunas...
pd.set_option("display.max_columns", None)

# Vamos carregar apenas algumas colunas do dataset original...
df = pd.read_csv('dados/dataset.csv', usecols = ['X1','X2','X3','X4','X5','X6'])

print(df.shape)

print()
print()

print(df.head)

print('#'*100)
# Vamos mostrar as categorias (valores únicos) por coluna...
for cols in df.columns:
    print(cols,':', len(df[cols].unique()), 'valores únicos ou categorias')

print()
print('#'*100)
# Vamos descobrir quantas colunas adicionais iremos obter após aplicar One-Hot-Encoding
# 123 (total de categorias) - 6 colunas originais = 117
print(pd.get_dummies(df, drop_first = True).shape)

print()
print('#'*100)
# Aplicamos One-Hot-Encoding
novo_df = pd.get_dummies(df, drop_first = True)
print(novo_df)
print('#'*100)
# Verificamos se algum valor nulo foi gerado

print(novo_df.isnull().any())

print('#'*100)

## Será que todas essas categorias são necessárias?
# É importante notar que esse processo pode resultar em um aumento significativo na dimensionalidade do 
# conjunto de dados. 

# No nosso caso, um dataframe original com apenas 6 colunas acabou se transformando em um dataframe 
# com 117 colunas após a aplicação do One-Hot Encoding. Esse aumento na dimensionalidade pode prejudicar a 
# eficiência e desempenho de certos algoritmos de aprendizado de máquina, especialmente se o conjunto de dados 
# já for grande.
# Dessa formasoe a questão da relevância e necessidade de todas as categorias presentes nas variáveis 
# categóric é questionávelas

# . Nem todas as categorias podem ser igualmente importantes para o problema em questão, e algumas podem 
# até mesmo ser redundantes ou irrelevantes. Portanto, é válido questionar se todas as categorias são 
# realmente necessárias e se é possível reduzir a dimensionalidade do conjunto de dados removendo categorias 
# menos relevantes.

#Ao avaliar a necessidade de reduzir a dimensionalidade, é importante considerar métodos como análise 
# exploratória de dados, técnicas de seleção de características e até mesmo algoritmos de redução de 
# dimensionalidade, como PCA (Análise de Componentes Principais), para garantir que o conjunto de dados 
# final seja eficiente e adequado para o modelo de aprendizado de máquina utilizadEm resumo é importante 
# notar que suma, enquanto o One-Hot Encoding é uma técnica útil para lidar com variáveis categóricas, 
# é fundamental ponderar sobre o impacto na dimensionalidade do conjunto de dados e questionar a relevância 
# de todas as categorias presentes.

# A coluna X1 possui 27 categorias. Vamos lista-las...
print(df.X1.value_counts(ascending = False))

print('#'*100)
# Vamos listas apenas as 10 categorias com mais registros
print(df.X1.value_counts(ascending = False).head(10))

print('#'*100)
# Colocamos essas 10 categorias que contém mais registros em uma nova variável Python... por exemplo: 
# relevantes
relevantes = [x for x in df.X1.value_counts().head(10).index]
print(relevantes)

print('#'*100)
# Vamos criar uma função que vai gerar as novas colunas com One-Hot-Encoding
def relevantes_OneHot(df, coluna, relevantes):
    for i in relevantes:
        df[coluna + "_" + i ] = np.where(df[coluna]==i,1,0)
# Executamos a função e aplicamos One-Hot-Encoding
relevantes_OneHot(df, 'X1', relevantes)
print(df)

print('#'*100)
### Vamos fazer isso para as demais Colunas X2 até X6
# Extraímos as 10 mais relevantes de X2
relevantes = [x for x in df.X2.value_counts().head(10).index]
# Executamos a função para aplicarmos o One-Hot-Encoding
relevantes_OneHot(df, 'X2', relevantes)
print(df)

print('#'*100)
# Fazendo o mesmo para X3
relevantes = [x for x in df.X3.value_counts().head(10).index]
relevantes
relevantes_OneHot(df, 'X3', relevantes)


print(df)

print('#'*100)
# Fazendo o mesmo para X4
relevantes = [x for x in df.X4.value_counts().head(10).index]
relevantes
relevantes_OneHot(df, 'X4', relevantes)

print(df)

print('#'*100)
# Fazendo o mesmo para X5
relevantes = [x for x in df.X5.value_counts().head(10).index]
relevantes
relevantes_OneHot(df, 'X5', relevantes)

print(df)

print('#'*100)
# Fazendo o mesmo para X6
relevantes = [x for x in df.X6.value_counts().head(10).index]
relevantes
relevantes_OneHot(df, 'X6', relevantes)
print(df)

print('#'*100)
# Verificamos se algum valor nulo foi gerado
df.isnull().any()
print(df.isnull().any())
print('#'*100)
print(df.shape)

print(df)


