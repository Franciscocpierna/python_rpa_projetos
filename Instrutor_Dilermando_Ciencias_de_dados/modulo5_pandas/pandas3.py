# Pandas - Noções básicas do pacote Pandas - Parte 3

# DataFrames

# Os DataFrames representam o elemento fundamental dos Pandas e são diretamente influenciados pela linguagem 
# de programação R, famosa por suas capacidades de análise de dados. Imagine um DataFrame como um conjunto 
# organizado de séries, todas elas compartilhando o mesmo índice. Essencialmente, é uma estrutura tabular
# bidimensional, onde os dados são organizados em linhas e colunas, proporcionando uma maneira poderosa e
#  flexível de lidar com conjuntos de dados complexos.

# Com o Pandas, podemos manipular e analisar esses conjuntos de dados de maneira eficiente, aproveitando a 
# riqueza de funcionalidades oferecidas por essa biblioteca. Desde operações simples de filtragem e seleção
# até transformações mais complexas e análises estatísticas, os DataFrames são a espinha dorsal de muitas 
# tarefas de ciência de dados e análise exploratória.

# Portanto, ao explorar esse tópico com o Pandas, estamos mergulhando no cerne da manipulação e análise 
# de dados, aproveitando uma ferramenta poderosa que nos permite extrair insights valiosos e tomar decisões 
# informadas com base nos dados disponív

# ### 3.1 O que são DataFrames?

# Os DataFrames são estruturas de dados bidimensionais no Pandas.
# Eles são semelhantes a tabelas de banco de dados ou planilhas do Excel.
# Cada coluna em um DataFrame é uma série.

# ### 3.2 Características dos DataFrames:

# - Bidimensional:  Possui linhas e colunas. Pode ser visto como uma coleção de séries.

# - Flexibilidade de Dados:  Pode conter diferentes tipos de dados em cada coluna.eis.

### 3.3 Criando DataFrames

#A partir de Arquivos CSV ou Excel

# df = pd.read_csv('dados.csv')
# df = pd.read_excel('dados.xls')


#A partir de Dicionários
# Importando o pacote Pandas
import pandas as pd

# Evitando mensagens de Warnings
import warnings
warnings.filterwarnings('ignore')
# Criando um dicionário
data = {'Nome': ['Alice', 'Bob', 'Carol'],
        'Idade': [25, 30, 22]}
# Converte um dicionário para um DataFrame
df = pd.DataFrame(data)
# Visualizar as 5  primeiras linhas do DataFrame criado
print(df.head())
print('#'*50)
#Verificando o tipo de dados do objeto df
print(type(df))
# Reorganizando as colunas do DataFrame
pd.DataFrame(data, columns = ['Idade', 'Nome'])
#Criando um outro dataframe, com os mesmos dados anteriores, acrescentando uma coluna e mudando o índice.
df2 = pd.DataFrame(data,
                columns = ['Nome', 'Idade', 'Escolaridade'],
                index = ['pessoa1', 'pessoa2', 'pessoa3'])
print('#'*50)                
print(df2)
print('#'*50) 
# Mostrar os valores do DataFrame
print(df2.values)
# Mostrar os tipos de dados do DataFrame
print('#'*50)  
df2.dtypes
# Mostrando as estatísticas do Dataframe (apenas dos valores numéricos)
print('#'*50)  
print(df2.describe())
# Mostrando as estatísticas do Dataframe (dos outros tipos de dados... Object)
df2.describe(include=['O'])
# Mostrar as colunas do DataFrame
print('#'*50)  
print(df2.columns)
print('#'*50)
# Mostrando apenas uma coluna específica do DataFrame (cuidade: a linguagem Python é case sensitive)
print(df2['Nome'])
# Se quiser mostrar mais de uma coluna, terá que passar os nomes das colunas dentro de uma lista.
# Por exemplo... vamos mostrar as colunas: Cidade e Ano
print('#'*50)
print(df2[ ['Nome', 'Idade']])
# Para exibir os índices...
print('#'*50)  
print(df2.index)
#Filtrando os dados pelo índice
print('#'*50)  
print(df2.filter(items = ['pessoa2'], axis=0))

### 3.4 Operações com Dataframes

#Filtragem de Dados
print('#'*50) 
filtro = df['Idade'] > 25
df_filtrado = df[filtro]
print(df_filtrado)

print('#'*50) 

#Ordenação de Dados

df_ordenado = df.sort_values(by='Idade', ascending=False)
print(df_ordenado)

print('#'*50) 

# Mostrando todo o dataFrame
print(df2)
print('#'*50) 
# Fatiando todas as linhas do índice pessoa1 até pessoa2
#Atenção: veja que o segundo parâmetro do slice não é exclusivo... ele é incluso no retorno.

print(df2['pessoa1':'pessoa2'])
print('#'*50) 
### 3.5 Manipulação de Dados

# Adição de Colunas
df2['Sexo'] = ['F', 'M', 'F']
df2['Profissão'] = ['Médica', 'Advogado', 'Dentista']
print(df2)
print('#'*50) 
#Remoção de Colunas

df2.drop(columns=['Profissão'], inplace=True)
print(df2)
print('#'*50)
### 3.6 Tratamento de Valores Ausentes

#Identificação de Valores Nulos

print(df2.isnull())

print('#'*50)
### 3.6 Tratamento de Valores Ausentes

#Identificação de Valores Nulos

print(df2.fillna(0, inplace=True))

# MENSAGEM DE AVISO:

# A mensagem de aviso aparece porque você está usando o método fillna() com inplace=True em uma DataFrame que contém arrays de tipo de dados dtype de objeto. O aviso sugere que o método fillna() pode estar causando rebaixamento de tipo de dados (downcasting), que será descontinuado em uma versão futura do pandas.

# Para evitar esse aviso, você pode fazer uma das seguintes opções:

# **Chamar o método infer_objects() antes de fillna():**

# Antes de usar fillna(), chame df2.infer_objects() para inferir os tipos de dados apropriados para os elementos no DataFrame:

# ```
# df2 = df2.infer_objects(copy=False)
# df2.fillna(0, inplace=True)
# ```

# **Alterar a opção pd.set_option():**

# Você pode optar pelo comportamento futuro, desativando o rebaixamento silencioso. Defina a opção future.no_silent_downcasting como True:

# ```
# pd.set_option('future.no_silent_downcasting', True)
# df2.fillna(0, inplace=True)
# ```

print('#'*50)
print(df2)
print('#'*50)

# Podemos também utilizar o NUMPY para inserir valores no dataframe...

import numpy as np

# Vamos inserir uma nova coluna no dataframe df2 com valores NaN

df2['Renda'] = pd.Series([np.nan] * len(df2))
print(df2)
print('#'*50)
#  Usando o NumPy para alimentar uma das colunas do dataFrame
## o método "arange" e cria um array de valores que crescem sequencialmente a partir de 0 até 2. 
## O argumento 3. especifica o valor final, 3 (borda exclusiva), mas o ponto decimal é importante aqui 
# para garantir que seja tratado como um número 
## float em vez de um inteiro. Isso significa que o array resultante terá os valores [0.0, 1.0, 2.0].

df2['Renda'] = np.arange(3.)
print(df2)
print('#'*50)
#Resumo estatístico (valores numéricos)
print(df2.describe())
print('#'*50)
#Resumo estatístico (dos outros tipos de dados... Object)
print(df2.describe(include=['O']))
print('#'*50)
### 3.7 Visualização de Dados com Dataframes

#Gráficos de Barras, Linhas e Pizzas

import matplotlib.pyplot as plt

df.plot(x='Nome', y='Idade', kind='bar')
plt.show()


df.plot(x='Nome', y='Idade', kind='line')
plt.show()

df.plot(x='Nome', y='Idade', kind='pie')
plt.show()
