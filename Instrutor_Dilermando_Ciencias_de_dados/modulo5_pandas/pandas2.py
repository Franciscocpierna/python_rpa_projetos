# Pandas - Noções básicas do pacote Pandas - Parte 2

# Series

# Vamos começar aprendendo sobre o primeiro tipo de dado: a Série. Para isso, iremos importar o Pandas e 
# examinar esse objeto em detalhes.

# A Série é bastante semelhante a uma matriz NumPy, construída sobre o objeto de matriz NumPy. No entanto, 
# o que a distingue é a capacidade de ter rótulos de eixos. Isso significa que pode ser indexada por um rótulo, 
# em vez de apenas por uma localização numérica. Além disso, não está limitada a manter dados numéricos, 
# podendo conter qualquer objeto Python arbitrários:"

# **2.1. O que são Séries?**

# As séries são uma estrutura de dados fundamental no Pandas.
# Elas são semelhantes a arrays NumPy, mas com rótulos de eixos (índices).
# Diferentemente de arrays, as séries podem conter qualquer tipo de dado.

# **2.2. Características das Séries:**

# - Indexação por Rótulos: Cada valor em uma série tem um rótulo associado (índice). Isso permite acessar 
#   os valores não apenas por posição numérica, mas também por rótulo.
# - Flexibilidade de Dados: As séries podem conter números, strings, datas, objetos Python, etc.

import numpy as np
import pandas as pd

### 2.1 Criando uma Serie

# A partir de uma lista:



labels = ['a', 'b', 'c']
minha_lista = [10, 20, 30]

serie_minha_lista = pd.Series(data=minha_lista, index=labels)
print(serie_minha_lista)

# A partir de um Array Numpy:

arr = np.array([10, 20, 30])
serie_arr = pd.Series(arr, index=labels)
print(serie_arr)

# A partir de um Dicionário:

d = {'a': 10, 'b': 20, 'c': 30}
serie_d = pd.Series(d)
print(serie_d)

### 2.2 Explorando uma Série

# Visualização dos Dados
# Mostrando a série (indices e dados)
print(serie_minha_lista)

# Mostrando os índices da série
print(serie_minha_lista.index)

# Mostrando apenas os dados
print(serie_minha_lista.values)

# Métodos úteis

# Primeiros valores
print(serie_minha_lista.head()) 

# Estatísticas resumidas
print(serie_minha_lista.describe()) 

### 2.3 Operações com Séries

#  Soma, Subtração, Multiplicação etc

serie_soma = serie_minha_lista + serie_arr

print(serie_soma)

#Filtragem de Dados

filtro = serie_minha_lista > 15
serie_filtrada = serie_minha_lista[filtro]
print(serie_filtrada)
print('#'*50)

### 2.4 Manipulação de Índices

#Renomeando Índices

serie_minha_lista.rename(index={'a': 'A', 'b': 'B'}, inplace=True)
print(serie_minha_lista)

print('#'*50)

# Reordenando índices

serie_minha_lista = serie_minha_lista.reindex(['c', 'B', 'a'])
print(serie_minha_lista)

print('#'*50)

### 2.5 Tratamento de Valores Ausentes

#Identificando valores Nulos

print(serie_minha_lista.isnull())

print('#'*50)

# Preenchimento de Valores Ausentes
serie_minha_lista.fillna(0, inplace=True)
print(serie_minha_lista)

print('#'*50)
### 2.6 Visualização de Dados com Séries

# Graficos de Linhas e de Barras
import matplotlib.pyplot as plt

serie_minha_lista.plot(kind='line')
serie_minha_lista.plot(kind='bar')
plt.show()
print('#'*50)
### 2.7 Exemplos Práticos

# Dados de Vendas




vendas = pd.Series([1000, 1500, 800], index=['Janeiro', 'Fevereiro', 'Março'])
print(vendas)
print('#'*50)
# Temperatura ao longo do tempo

temperatura = pd.Series([25, 28, 30, 27], index=pd.date_range(start='2024-01-01', periods=4, freq='D'))
print(temperatura)