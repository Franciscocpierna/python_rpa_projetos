

## <font color='green'>Projeto 6 - Marketing para Instituições Financeiras - Parte 02</font>
## <font color='green'>Realizando a Análise Exploratória dos Dados</font>

# Importação dos Pacotes necessários para este projeto
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# Carrega o dataset
df = pd.read_csv("dados/bank-full.csv") 

print(df.shape)

print('#'*100)

print(df.head())
print('#'*100)
## Análise Exploratória

print(df.info())

print('#'*100)

# Temos valores nulos?
print(df.isna().any())

print('#'*100)

# Temos valores nulos?
print(df.isna().sum())
print('#'*100)


# Não usaremos a coluna ID. Portanto, vamos removê-la.
df.drop(["id"], axis = 1, inplace = True)

print(df.columns)

print('#'*100)

## Corrigindo a coluna "maritalEdu" 
# Esta coluna apresenta duas informações: Estado Civil (marital) e Nivel Educacional (education). 
# Vamos separar em duas colunas distintas.
print(df.head())
print('#'*100)
# Vamos fazer o split da coluna "maritalEdu" e criarmos a coluna "marital" com o primeiro elemento antes do
# hífen (-)
df['marital'] = df["maritalEdu"].apply(lambda x:x.split("-")[0])
print(df.head())
print('#'*100)


# Vamos fazer o split da coluna "maritalEdu" e criarmos a coluna "education" com o segundo elemento antes 
# do hífen (-)
df['education'] = df["maritalEdu"].apply(lambda x:x.split("-")[1])

print(df.head())
print('#'*100)
# Drop da coluna "jobedu" 
df.drop(["maritalEdu"], axis = 1, inplace = True)


print(df.head())


print(df.shape)

print('#'*100)




## Salvando os Dados desta Etapa 2

# Salvando os dados
df.to_csv('dados/bank-full_parte2.csv')

