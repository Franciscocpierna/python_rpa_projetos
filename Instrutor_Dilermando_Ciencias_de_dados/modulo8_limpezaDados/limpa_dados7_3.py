## <font color='green'>Projeto 7 - Diabetes dos Índios Pima - Parte 03</font>
## <font color='green'>Começando a Limpeza dos Dados - B</font>

# Importando os Dados
import math
import numpy as np
import pandas as pd

# Criamos uma lista para identificar valores ausentes
lista_labels_valores_ausentes = ["n/a", "na", "NA", "undefined"]

# Carregando o Dataset
dataset = pd.read_csv("dados/dataset_parte2.csv", na_values = lista_labels_valores_ausentes)

# Carregando o módulo que contém as funções específicas para limpeza de Dados
from limpeza_dados import *
print('#'*100)
print(dataset.head())

# Como o arquivo salvo não possuia id, ao sarvar o arquivo, o pandas cria uma nova coluna de identificação e ele chama de Unnamed:0 
# Vamos removê-la.
dataset.drop(["Unnamed: 0"], axis = 1, inplace = True)

print('#'*100)
print(dataset.head())

print('#'*100)
print(dataset.info())
print(dataset.shape)

print('#'*100)
# Verificando os valores ausentes no dataset com as funções:
# Porcentual total de valores ausentes
print()

print('#'*100)

print(calcular_porcentagem_valores_ausentes(dataset))

print('#'*100)
# Porcentagem de valores ausentes por coluna
print(relatorio_valores_ausentes_por_coluna(dataset))
print('#'*100)

### Limpando os Dados - B

# Podemos ver que a coluna "Insulin" (Insulina) possui quase 50% de valores nulos. Portanto, como estamos falando de um valor muito superior 
# a 30% então vamos apagar (drop) a coluna inteira.

# Função para remover colunas

print(remover_colunas(dataset, ["Insulin"]))

print('#'*100)
# Porcentagem de valores ausentes por coluna
print(relatorio_valores_ausentes_por_coluna(dataset))

print('#'*100)
# Verificação de Assimetria dos dados
print(dataset.skew())


# **REGRA:** 
# - Valores com com ALTA assimetria fazemos a imputação de dados com a MEDIANA.
# - Valores com média ou baixa assimetria, utilizamos a MÉDIA.


# Para este dataset:

# - Acima de 0.55           --> Alta Assimetria     
# - Igual ou abaixo de 0.55 --> Média/Baixa Assimetria

# Portanto:
# - ALTA ASSIMETRIA (SkinThickness, BMI)
# - MÉDIA/BAIXA ASSIMETRIA (BloodPressure, Glucose)






print('#'*100)
# ALTA ASSIMETRIA (SkinThickness, BMI) --> Preenchimento com MEDIANA
print(preencher_ausentes_com_mediana(dataset, "BMI"))



print('#'*100)
# ALTA ASSIMETRIA (SkinThickness, BMI) --> Preenchimento com MEDIANA
print(preencher_ausentes_com_mediana(dataset, "SkinThickness"))

print('#'*100)
# MÉDIA/BAIXA ASSIMETRIA (BloodPressure, Glucose) --> Preenchimento com MÉDIA

print(preencher_ausentes_com_media(dataset, "BloodPressure"))

print('#'*100)
# MÉDIA/BAIXA ASSIMETRIA (BloodPressure, Glucose) --> Preenchimento com MÉDIA
print(preencher_ausentes_com_media(dataset, "Glucose"))

print('#'*100)

# Porcentagem de valores ausentes por coluna
print(relatorio_valores_ausentes_por_coluna(dataset))

# Salvando os dados
dataset.to_csv('dados/dataset_parte3.csv')


