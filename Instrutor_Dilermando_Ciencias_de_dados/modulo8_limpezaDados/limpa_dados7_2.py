## <font color='green'>Projeto 7 - Diabetes dos Índios Pima - Parte 02</font>
## <font color='green'>Começando a Limpeza dos Dados - A</font>

# Importando os pacotes/blibliotecas
import math
import numpy as np
import pandas as pd

# Criamos uma lista para identificar valores ausentes
lista_labels_valores_ausentes = ["n/a", "na", "NA", "undefined"]

# Carregando o Dataset
dataset = pd.read_csv("dados/diabetes.csv", na_values = lista_labels_valores_ausentes)

# Carregando o módulo que contém as funções específicas para limpeza de Dados
from limpeza_dados import *

### Limpando os Dados - A

print(dataset.head())

print('#'*100)
print(dataset.shape)

print('#'*100)
print(dataset.info())
print('#'*100)
print(dataset.isnull().sum())
#
print('#'*100)
# Verificando os valores ausentes no dataset com as funções:
# Porcentual total de valores ausentes
calcular_porcentagem_valores_ausentes(dataset)

print('#'*100)
# Porcentagem de valores ausentes por coluna
relatorio_valores_ausentes_por_coluna(dataset)
print('#'*100)
print(dataset.sample(30))
print('#'*100)
# Verificando o toal de valores iguais a zero por coluna

dataset.apply(lambda x: (x==0).sum())
print('#'*100)

#Notamos que aqui não se trata de um dataset com valores nulos (ausência de dados). **Aqui é o caso de 
# ausência de informação**. 

#Esse é o tipo de limpeza de dados mais difícil a ser realizado, pois temos que ter a certeza que do que 
#se trata: o "zero" é informação ou ausência de informação?

# Vamos alterar essa ausência de informação em ausência de dados!
# coluna GLUCOSE
dataset["Glucose"] = dataset["Glucose"].apply(lambda x: np.nan if x == 0 else x)
# coluna BLOODPRESSURE
dataset["BloodPressure"] = dataset["BloodPressure"].apply(lambda x: np.nan if x == 0 else x)
# coluna SKINTHICKNESS
dataset["SkinThickness"] = dataset["SkinThickness"].apply(lambda x: np.nan if x == 0 else x)
# coluna INSULIN
dataset["Insulin"] = dataset["Insulin"].apply(lambda x: np.nan if x == 0 else x)
# coluna BMI
dataset["BMI"] = dataset["BMI"].apply(lambda x: np.nan if x == 0 else x)
print(dataset["BMI"])



# Verificando os valores ausentes no dataset com as funções:
# Porcentual total de valores ausentes
print('#'*100)
print(calcular_porcentagem_valores_ausentes(dataset))

print('#'*100)
# Porcentagem de valores ausentes por coluna
print(relatorio_valores_ausentes_por_coluna(dataset))

# Salvando os dados
dataset.to_csv('dados/dataset_parte2.csv')

