# Projeto 14 - Cifose - Random Forest


### Vamos trabalhar novamente com dataset sobre Cifose (Kyphosis) disponível no Kaggle
# Para exemplificarmos a utilização de Random Forest (que se trata de um algoritmo que vai criar 
# muitas árvores de decisão), vamos trabalhar com o mesmo dataset que utilizamos para Árvores de Decisão 
# de Cifose, disponível em Kaggle (fonte: https://www.kaggle.com/datasets/abbasit/kyphosis-dataset).

# A imagem abaixo ilustra o problema ocasionado pela cifose:

# ![title](imagens/cifose2.jpg)

# ### Descrição do Problema

# Cifose é uma curvatura convexa anormalmente excessiva da coluna vertebral, também conhecida como 
# "corcunda". O dataset de cifose possui 81 linhas e 4 colunas, representando dados sobre crianças 
# que passaram por cirurgia corretiva na coluna vertebral. O conjunto de dados contém 3 entradas e 1 saída.

# ENTRADAS:
# - Age (idade): em meses
# - Number (número): o número de vértebras envolvidas
# - Start (inicio): o número da primeira (mais superior) vértebra operada.

# SAÍDAS:
# - kyphosis (Cifose): um fator com níveis "ausente" (absent) ou "presente" (present), indicando se uma 
# cifose (um tipo de deformação) estava presente após a operação.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Para treinamento do modelo
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix

# para evitar mensagens de alerta/warnings.
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Carregar o módulo de funções para limpeza de dados
from limpeza_dados import *

# Carregando o Dataset
df = pd.read_csv('dados/kyphosis.csv')

print(df.head())


print('#'*100)

print(df.tail())

print('#'*100)

print(df.describe())

print('#'*100)

print(df.info())

print('#'*100)
# verificando se existe algum valor nulo

calcular_porcentagem_valores_ausentes(df)


## Exploração dos Dados (EDA)

# Uma contagem simples dos pacientes

# Calcular a contagem de cada categoria
counts = df['Kyphosis'].value_counts()

# Plotar o gráfico de barras
sns.barplot(x=counts.index, y=counts.values)

# Adicionar rótulos aos eixos
plt.xlabel('Kyphosis')
plt.ylabel('Counts')

# Mostrar o gráfico
plt.show()

# análise da distribuição
sns.pairplot(df,hue='Kyphosis',palette='Set1')
plt.show()
print('#'*100)
# Análise da Correlação

# Para mostrar o mapa de correlação temos que fazer uma modificação dos dados da variável Kyphosis
# Temos que transforma-los em valores numéricos

# Vamos fazer uma cópia do dataset
df_numerico = df.copy()

# Agora nessa cópia, vamos alterar os valores: absent = 0  e present = 1
df_numerico['Kyphosis'] = df_numerico['Kyphosis'].map({'absent': 0, 'present': 1})

# Agora sim conseguimos mostrar o mapa de correlação do dataset alterado
sns.heatmap(df_numerico.corr(), annot = True)

plt.show()

## Divisão em Teste e Treino

X = df.drop('Kyphosis',axis=1)
y = df['Kyphosis']

# vamos reservar 30% do dataset para teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

## Criando o Modelo com Random Forest

# Criando o Modelo
rf = RandomForestClassifier(n_estimators=100)

# O parâmetro **n_estimators** é um dos hiperparâmetros mais importantes no algoritmo Random Forest, que é utilizado para controlar o 
# número de árvores na floresta. Em termos simples, um modelo de Random Forest funciona construindo várias árvores de decisão durante o 
# treinamento e, em seguida, combinando suas previsões para obter uma previsão final mais robusta e geralmente mais precisa.

# Portanto, n_estimators especifica quantas árvores de decisão devem ser construídas no processo de treinamento do Random Forest. 
# Quanto maior o número de estimadores, mais complexo será o modelo e mais preciso ele pode se tornar, até um certo ponto

# . No entanto, aumentar o número de estimadores também pode aumentar o tempo de treinamento e o uso de memória do modelo.

# Em resumo, n_estimators é um parâmetro que controla o trade-off entre a complexidade do modelo e seu desempenho, e geralmente 
# é ajustado durante o processo de ajuste de hiperparâmetros para encontrar o valor que proporciona o melhor equilíbrio entre 
# precisão e eficiência.

# Treinando o Modelo
rf.fit(X_train,y_train)

## Predição e Avaliação
predictions = rf.predict(X_test)

print(classification_report(y_test,predictions))
acu = rf.score(X_test, y_test)
# Acurácia do Modelo
print(f"Acurácia do Modelo = {acu:.1%}")

print('#'*100)

# Mostrando a matriz de confusão (textualmente)
cm = confusion_matrix(y_test,predictions)
print(cm)

# Mostrando a matriz de confusão (graficamente)
sns.heatmap(cm, annot = True)
plt.show()

# **Verdadeiro: 0, Previsto: 0 (19):** Isso significa que o modelo classificou corretamente 19 amostras como Classe 0.

# **Verdadeiro: 0, Previsto: 1 (2):** Isso significa que o modelo classificou incorretamente 2 amostras que eram da Classe 0 como Classe 1.

# **Verdadeiro: 1, Previsto: 0 (3):** Isso significa que o modelo classificou incorretamente 3 amostras que eram da Classe 1 como Classe 0.

# **Verdadeiro: 1, Previsto: 1 (1):** Isso significa que o modelo classificou corretamente 1 amostras como Classe 1.

