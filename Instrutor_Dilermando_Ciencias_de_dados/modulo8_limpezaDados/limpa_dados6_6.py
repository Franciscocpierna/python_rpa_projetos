

# <font color='green'>Projeto 6 - Marketing para Instituições Financeiras - Parte 06</font>
## <font color='green'>Tratamento de Valores Ausentes - D</font>

# Importação dos Pacotes necessários para este projeto
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Carrega o dataset
df = pd.read_csv("dados/bank-full_parte5.csv") 

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

#Falta apenas tratarmos a coluna "target" (alvo). É a coluna que indica se a campanha de market foi ou não 
# bem sucedida. Se o cliente optou pelo produto ou não.

# Valores ausentes
print(df.target.isnull().sum())

## Limpeza Concluída...


print('#'*100)
# Calcula o percentual
print(df.target.isnull().mean()*100)

print('#'*100)
# O percentual é baixo (e a variável é o alvo da nossa análise) não podemos eliminar a coluna.
# Como nos casos anterios, nos sobra duas alternativas: 1) Eliminar os registros com valores ausentes
# (nesse caso perderíamos 7 linhas no dataset) ou  2) aplicar imputação dos dados ausentes.

# Você tem condições de saber o que o cliente decidiu fazer (optou ou não pelo produto)?

# Nesse caso, a eliminação dos registros parece ser a escolha mais apropriada.

# Vamos eliminar os registros com valores ausentes (dropar os registros).
df.dropna(subset = ["target"], inplace = True)
print(df.head())
print('#'*100)
# Verifca valores NA
print(df.isnull().sum())

# Salvando os dados
df.to_csv('dados/bank-full_parte6.csv')


