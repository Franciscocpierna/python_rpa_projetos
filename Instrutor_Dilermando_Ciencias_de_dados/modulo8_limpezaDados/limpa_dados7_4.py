## <font color='green'>Projeto 7 - Diabetes dos Índios Pima - Parte 04</font>
## <font color='green'>Começando a Limpeza dos Dados - C</font>

# Importando os Dados
import math
import numpy as np
import pandas as pd

# Criamos uma lista para identificar valores ausentes
lista_labels_valores_ausentes = ["n/a", "na", "NA", "undefined"]

# Carregando o Dataset
dataset = pd.read_csv("dados/dataset_parte3.csv", na_values = lista_labels_valores_ausentes)

# Carregando o módulo que contém as funções específicas para limpeza de Dados
from limpeza_dados import *

print('#'*100)
print(dataset.head())
print('#'*100)
# Como o arquivo salvo não possuia id, ao sarvar o arquivo, o pandas cria uma nova coluna de identificação e ele chama de Unnamed:0 
# Vamos removê-la.
dataset.drop(["Unnamed: 0"], axis = 1, inplace = True)
print(dataset.head())
print('#'*100)
print(dataset.shape)
print('#'*100)
print(dataset.info())
print('#'*100)
# Verificando os valores ausentes no dataset com as funções:
# Porcentual total de valores ausentes

print(calcular_porcentagem_valores_ausentes(dataset))
print('#'*100)
# Porcentagem de valores ausentes por coluna
print(relatorio_valores_ausentes_por_coluna(dataset))
print('#'*100)
### Limpando os Dados - C 
### Analisando valores Outliers

# Cria um objeto para tratar valores outliers
trata_outlier = ManipuladorDeOutliers(dataset)
# Cria uma lista de colunas float64
lista_colunas = dataset.select_dtypes('float64').columns.tolist()


print(lista_colunas)

print('#'*100)
# Mostra uma visão geral dos outliers
print(trata_outlier.gerar_visao_geral(lista_colunas))

print('#'*100)
# Substituição dos outliers por margens definidas
trata_outlier.substituir_outliers_por_limites(lista_colunas)
# Mostra uma visão geral dos outliers
print(trata_outlier.gerar_visao_geral(lista_colunas))

# Salvando os dados
dataset.to_csv('dados/dataset_parte4.csv')