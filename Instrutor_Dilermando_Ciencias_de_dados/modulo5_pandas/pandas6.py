# Pandas - Noções básicas do pacote Pandas - Parte 6
## Funções e Métodos

### 6.1 Introdução às Funções e Métodos

# **Funções:**

# Realizam operações específicas em colunas ou linhas de um DataFrame. Podem ser aplicadas a uma série ou
# a todo o DataFrame.

# **Métodos:**
# São funções específicas do Pandas que operam em DataFrames. São chamados usando a sintaxe df.metodo().

### 6.2 Exemplo Inicial: Criando um DataFrame Simples


import pandas as pd

data = {'Nome': ['Alice', 'Bob', 'Carol'],
        'Idade': [25, 30, 22],
        'Salário': [5000, 6000, 7000]}

df = pd.DataFrame(data)

print(df.head())

print('#'*50)
### 6.3 Funções e Métodos

# **a) unique() e nunique()**

# - unique(): Retorna os valores únicos em uma coluna.

# - nunique(): Retorna o número de valores únicos em uma coluna.

# Retorna os valores únicos na coluna especificada
print(df['Nome'].unique())

print('#'*50)

# Retorna o número de valores únicos na coluna especificada
print(df['Idade'].nunique())

print('#'*50)
# **b) value_counts()**

# - Retorna a contagem de valores únicos em uma coluna.
print(df['Nome'].value_counts())
print('#'*50)

# **c) apply()**

# - Aplica uma função a cada elemento de uma coluna.

# definindo uma função
def dobrar_salario(salario):
    return salario * 2

# aplicando a função
df['Salário_Dobrado'] = df['Salário'].apply(dobrar_salario)
print(df)

# **d) Funções de Agregação**

# sum(), mean(), max(), min(), idxmax(), idxmin()
print('#'*50)
print(f" Salário  {df['Salário'].sum()}")
print(f" Idade  {df['Idade'].mean()}")
print(f" Sálario  {df['Salário'].max()}")
print(f" Idade  {df['Idade'].min()}")
print(f" Sálario  {df['Salário'].idxmax()}")

print('#'*50)
# **e) Operações Aritméticas**

# add(), mul(), div()
df['Salário_Aumentado'] = df['Salário'].add(1000)
print(df)

print('#'*50)
# **f) map()**

# Mapeia valores de uma coluna para outros valores.

genero_map = {'Alice': 'F', 'Bob': 'M', 'Carol': 'F'}
df['Gênero'] = df['Nome'].map(genero_map)
print(df)
print('#'*50)
# **g) where()**

# Substitui valores com base em uma condição.
df['Salário_Alto'] = df['Salário'].where(df['Salário'] > 6000, other=0)
print(df)

print('#'*50)
#**h) copy()**

#Cria uma cópia independente do DataFrame.
df_copia = df.copy()
print(df)
print('#'*50)
print(df_copia)

# O comando `df.copy()` é utilizado para criar uma cópia profunda do DataFrame `df`. 

# Essa cópia é independente do DataFrame original, o que significa que quaisquer alterações feitas na 
# cópia não afetarão o DataFrame original e vice-versa. 

# É útil utilizar `df.copy()` quando se deseja modificar um DataFrame sem modificar o original, preservando
#  assim os dados originais. 



