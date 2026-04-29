# <font color='green'>Projeto 7 - Diabetes dos Índios Pima - Parte 01</font>
## <font color='green'>Instalando os Pacotes e Carregando os Dados</font>

# Imports
import math
import numpy as np
import pandas as pd
import openpyxl

## Carregando os Dados

# # ### Contexto
# -------
# Este conjunto de dados é originalmente do Instituto Nacional de Diabetes e Doenças Digestivas e Renais. 
# O objetivo do conjunto de dados é prever, de forma diagnóstica, se um paciente tem diabetes ou não, com 
# base em certas medições diagnósticas incluídas no conjunto de dados. Várias restrições foram colocadas na 
# seleção dessas instâncias de um banco de dados maior. Em particular, todos os pacientes aqui são mulheres 
# com pelo menos 21 anos de idade de herança indígena Pima.

# ### Conteúdo
# --------
# O conjunto de dados consiste em várias variáveis preditoras médicas e uma variável-alvo, o Resultado 
# (target). As variáveis preditoras incluem o número de gestações que a paciente teve, seu IMC, nível 
# de insulina, idade, e assim por diante.

# ### Base de Dados / Fonte:
# --------
# Este dataset é público  e está disponível em Kaggle no link: 
# https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
# O arquivo `diabets.csv` está disponível na pasta `dados` (como recurso dessa aula).

# Criamos uma lista para identificar valores ausentes
lista_labels_valores_ausentes = ["n/a", "na", "NA", "undefined"]

# Carrega o dataset
dataset = pd.read_csv("dados/diabetes.csv", na_values = lista_labels_valores_ausentes)

print(dataset.shape)

print('#'*100)
print(dataset.head())

print('#'*100)
print(dataset.info())

print('#'*100)
print(dataset.describe())
print('#'*100)

# Verificar os valores ausentes no dataset

print('#'*100)
# Para que todas as funções lá criadas fiquem disponível, temos que importar da seguinte forma:
# Carregando o arquivo de descrição das funções de limpeza de dados
descricao = pd.read_excel("descricao_funcoes.xlsx")

print(descricao.shape)

print('#'*100)
print(descricao)

print('#'*100)
print('#'*100)



print('#'*100)