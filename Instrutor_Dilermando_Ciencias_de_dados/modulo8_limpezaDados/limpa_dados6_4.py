# <font color='green'>Projeto 6 - Marketing para Instituições Financeiras - Parte 04</font>
## <font color='green'>Tratamento de Valores Ausentes - B</font>

# Importação dos Pacotes necessários para este projeto
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
# Carrega o dataset
df = pd.read_csv("dados/bank-full_parte3.csv") 
print(df.shape)

print('#'*100)
print(df.head())

print('#'*100)
# Como removemos o id, ao sarvar o arquivo, o pandas cria uma nova coluna de identificação e ele chama de Unnamed:0 
# Vamos removê-la.

df.drop(["Unnamed: 0"], axis = 1, inplace = True)

print(df.head())

print('#'*100)
print(df.info())

print('#'*100)
# Temos valores nulos?
print(df.isna().any())


print('#'*100)
# Temos valores nulos?
print(df.isna().sum())

print('#'*100)

## Tratamento de Valores Ausentes
#A próxima coluna que vamos tratar com valores ausentes é a do mês (month)

# Valores ausentes na variável
print(df.month.isnull().sum())

print('#'*100)
# Percentual de valores ausentes
print(df.month.isnull().mean()*100)

# Como o percentual é menor que 30% não é indicada a deleção da coluna. 
# Temos aqui também duas opções: 1) Eliminar os registros com valores ausentes (nesse caso perderíamos 23 linhas no dataset) ou 2) Aplicar imputação de dados.
# Para este caso, vamos aqui também, fazer a imputação de dados.

# Tipo da variável

print(df.month.dtypes)
print('#'*100)
# Categorias da variável
print(df.month.value_counts())


print('#'*100)

#Ao analisarmos a distribuição e contagem dos meses registrados no dataset, percebemos que existe uma maior 
#qtd de registros no mês de maio (may). Para que não haja mudança no padrão de distribuição dos dados 
#no dataset, e por ser a quantidade de valores ausentes pequena, podemos fazer a imputação dos dados utilizando
# aqui também, a moda.

# Vamos imputar com a moda, o valor mais frequente da variável, pois são poucos registro
print(df.month.mode())
# Imputação com a moda

print(df.month.fillna("may", inplace = True))

print(df.month.isnull().sum())
# Salvando os dados
df.to_csv('dados/bank-full_parte4.csv')

print('#'*100)


