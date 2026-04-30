## Transformação e Codificação de Variáveis...
## Mini-Projeto 8 - Count/Frequency Encoding

# Importação dos Pacotes (dupla dinâmica)
import pandas as pd
import numpy as np

# Mostrando todas as colunas do dataframe
print(pd.set_option('display.max_columns', None))

# Carregando os dados de algumas colunas específicas... no caso: X1, X2 e X3
df = pd.read_csv('dados/dataset.csv', usecols = ['X1','X2','X3'])
# Qual o formato deste dataframe carregado
print(df.shape)
print('#'*100)
print(df.head())
print('#'*100)
# Mostrando os valores únicos dentro da coluna X1
print(len(df.X1.unique()))
print('#'*100)
# Contando os valores únicos para cada uma das colunas
for i in df.columns:
    print(i,"-", len(df[i].unique()), "valores únicos ou categorias")

print('#'*100)
# Contagem/frequência das categorias da coluna X1
frequencia = df.X1.value_counts().to_dict()
# Vizualizando o dicionário que contem a frequência de cada categoria.
print(frequencia)
print('#'*100)
# Vamos fazer o "replace" de cada categoria pela contagem/frequencia na coluna X1
df.X1 = df.X1.map(frequencia)
print(df)
print('#'*100)
### Pare e faça o "replace" pela frequência nas demais colunas: X2 e X3

# Importante que você tente fazer antes de ver os resultados abaixo. Praticar... fazer, ajuda no processo 
# de fixação dos procedimentos.
# Vamos ao processo...

# Contagem/frequencia das categorias da coluna X2
frequencia = df.X2.value_counts().to_dict()

# Agora fazemos o replace de cada categoria pela contagem/frequencia na coluna X2
df.X2 = df.X2.map(frequencia)
# Contagem/frequencia das categorias da coluna X3
frequencia = df.X3.value_counts().to_dict()

# Agora fazemos o replace de cada categoria pela contagem/frequencia na coluna X3
df.X3 = df.X3.map(frequencia)

# Ao final, para validarmos o processo... verificamos se algum valor nulo foi gerado
df.isnull().any()
# O processo foi concluído com Sucesso.
# Mostrando o DataFrame resultante...

print(df)
