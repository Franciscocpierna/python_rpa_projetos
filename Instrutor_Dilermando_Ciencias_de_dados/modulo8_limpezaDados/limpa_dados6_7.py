# <font color='green'>Projeto 6 - Marketing para Instituições Financeiras - Parte 07</font>
## <font color='green'>Tratamento de Valores Ausentes  - E</font>

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Carrega o dataset
df = pd.read_csv("dados/bank-full_parte6.csv") 

print(df.shape)

print('#'*100)
print(df.head())


print('#'*100)
# Como removemos o id, ao sarvar o arquivo, o pandas cria uma nova coluna de identificação e ele chama 
# de Unnamed:0 
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
# Vamos analisar a coluna pdays (segundo a descrição no site que obtivemos o dataset, pdays (*past days*) 
# indica o número de dias que se passaram desde que o cliente foi contatado pela última vez em uma campanha 
# anterior (numérico; 999 significa que o cliente não foi contatado anteriormente). 

# Valores ausentes
print(df.pdays.isnull().sum())

print('#'*100)

# Describe
print(df.pdays.describe())
print('#'*100)

# Segundo a descrição, uma vez contactado, registra-se a data... No próximo contato, se houver, neste 
# campo será registrado o número de dias transcorridos.  Nesse caso... faz algum sentido o valor -1?
# Portanto... para este caso em específico... -1 indica um valor ausente. Temos que tratá-lo.

# Vamos fazer relace de -1 por NaN
#df.pdays = df.pdays.replace({-1.0:np.NaN}) erro versão mais nova numpy
df.pdays = df.pdays.replace({-1.0: np.nan})
# Valores ausentes
print(df.isnull().sum())
# Calcula o percentual
print(df.pdays.isnull().mean()*100)
print('#'*100)
# Com essa constatação de que mais de 80% dos valores aqui estão "ausentes", qual a melhor alternativa?
# ELIMINAR A COLUNA 'PDAYS', pois está acima de 30% de valores ausentes.

# Drop da coluna "pdays" 
df.drop(["pdays"], axis = 1, inplace = True)

# Valores ausentes
print(df.isnull().sum())
# Salvando os dados
df.to_csv('dados/bank-full_final.csv')

print('#'*100)

print('#'*100)

