# Pandas - Noções básicas do pacote Pandas - Parte 4

# Groupby

# O método groupby permite agrupar linhas de dados em conjunto e chamar funções agregadas

# **4.1 Agrupamento de Dados**

# O método groupby permite agrupar linhas de um DataFrame com base em valores específicos de uma ou mais 
# colunas. É semelhante à cláusula GROUP BY em SQL.

# **4.2 Sintaxe Básica**

# A sintaxe geral é: `df.groupby('coluna')`.

# Você pode agrupar por uma única coluna ou por várias colunas passando uma lista de colunas.

# **4.3 Operações após o Agrupamento**

# Após o agrupamento, você pode aplicar funções de agregação, como sum(), mean(), count(), etc. Essas 
# funções resumem os dados dentro de cada grupo.

import pandas as pd
# Criação de um novo DataFrame a partir de um dicionário
data = {'Empresa':['pyPRO', 'Fatec', 'pyPRO', 'pyPRO', 'eDigital', 'Fatec'],
       'Classe':['Júnior','Júnior','Pleno','Pleno','Sênior','Sênior'],
       'Nome':['Jorge','Carlos','Roberta','Patrícia','Bruno','Vera'],
       'Venda':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

print(df)

print('#'*50)
#** Agora, você pode usar o método .group by () para agrupar as linhas em conjunto com base em um nome de 
# coluna. Por exemplo, vamos agrupar com base na empresa. Isso criará um objeto DataFrameGroupBy:**
df2=df.groupby('Empresa')
print(df2)

# Você pode salvar este objeto como uma nova variável:
print('#'*50)
por_companhia = df.groupby("Empresa")
print(por_companhia.mean(numeric_only=True))


# Você também pode usar a função `agg()` (abreviação de "aggregate") como uma alternativa à função `mean()`. 
# A função `agg()` permite especificar várias funções de agregação para aplicar a cada grupo. Por exemplo, 
# para calcular a média e a soma das vendas para cada empresa, você pode fazer assim:
print('#'*50)
print(por_companhia.agg({'Venda': ['mean', 'sum']}))
print('#'*50)
#Mais exemplos de métodos agregados:
print(por_companhia.std(numeric_only=True))
print('#'*50)
por_companhia.min(numeric_only=True)
print('#'*50)
print(por_companhia.max(numeric_only=True))
print('#'*50)
print(por_companhia.count())
print('#'*50)
print(por_companhia.describe())

print('#'*50)
print(por_companhia.describe().transpose())
print('#'*50)
print(por_companhia.describe().transpose()['pyPRO'])

