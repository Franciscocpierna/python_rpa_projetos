## Noções de Matemática - Estatística e Probabilidade - Parte 1

#Ao longo desse módulo vamos trabalhar uma introdução ao universo da Estatistica e Probabilidade voltadas para 
# Ciência de dados. Os tópicos que abordaremos em cada um dos Notebooks (Partes) são os seguintes:

# #### Introdução à Estatística
# - 1.1 O que é Estatística?
# - 1.2 Conceitos básicos
# - 1.3 Objetivos da estatística
# - 1.4 População e amostra
# - 1.5 Variáveis

# #### Tipos de Dados
# - 2.1 Dados qualitativos e quantitativos
# - 2.2 Dados discretos e contínuos

# #### Medidas de Tendência Central
# - 3.1 Média
# - 3.2 Mediana
# - 3.3 Moda

# #### Medidas de Dispersão
# - 4.1 Variância
# - 4.2 Desvio padrão
# - 4.3 Intervalo interquartil

# #### Distribuições de Probabilidade
# - 5.1 Distribuição normal
# - 5.2 Distribuição binomial
# - 5.3 Distribuição de Poisson

# #### Probabilidade e Inferência Estatística
# - 6.1 Conceitos básicos
# - 6.2 Regra da adição
# - 6.3 Regra da multiplicação
# - 6.4 Eventos independentes e dependentes

# #### Amostragem e Estimação
# - 7.1 Amostragem aleatória simples
# - 7.2 Estimativa de parâmetros populacionais
# - 7.3 Intervalo de confiança

# #### Teste de Hipóteses
# - 8.1 Conceitos básicos de teste de hipóteses
# - 8.2 Teste de hipóteses para uma média populacional
# - 8.3 Teste de hipóteses para duas médias populacionais

# #### Regressão Linear
# - 9.1 Análise de regressão simples
# - 9.2 Coeficiente de correlação
# - 9.3 Coeficiente de determinação

# #### Análise de Variância (ANOVA)
# - 10.1 Conceitos básicos de ANOVA

# Vamos começar com uma introdução a Estatística...

## 1. Introdução à Estatística

# A estatística é uma disciplina que envolve a coleta, organização, análise, interpretação e 
# apresentação de dados. Na Ciência de Dados, a estatística desempenha um papel fundamental ao 
# lidar com a compreensão e a extração de informações de conjuntos de dados.

# **1.1 O que é Estatística?**

# A estatística é o estudo de como lidar com a incerteza por meio da análise de dados. 
# Ela envolve a aplicação de métodos estatísticos para resumir, analisar e interpretar os dados, 
# permitindo que sejam feitas inferências sobre as populações das quais os dados foram coletados.

# Um conceito importante que devemos sempre se lembrar quando trabalhamos com estatística é:
#  “A estatística deve simplificar, e não complicar, a interpretação dos dados”.

# A **estatística descritiva** é representada por um conjunto de métodos que descreve os dados coletados
#  — e tem por objetivo fazer com que eles sejam compreendidos mais facilmente. Isso se dá por meio da 
# organização, simplificação, descrição e apresentação dos dados. Tabelas, gráficos e medidas que 
# resumem os dados brutos são suas ferramentas. Ex: a média de gastos em compras online é de R$ 93,05.

# A **estatística inferencial** é representada por um conjunto de métodos de análise que nos permite
#  tirar conclusões (inferir) sobre a população com base em apenas parte dela (amostra). 
# Alguns exemplos de análises ou testes inferenciais são: qui-quadrado, anova, teste t, correlação,
#  regressão linear, regressão logística etc.  Ex: Quem compra um determinado produto A, 
# tem 90% de chance de se interessar por um outro produto B.

#**1.2 Conceitos básicos**

# Alguns conceitos básicos na estatística são essenciais para uma compreensão adequada da disciplina.
#  Aqui estão alguns deles:

# •	**Dados**: São observações ou informações coletadas a partir de uma fonte. Os dados podem ser
#  representados de forma numérica, categórica ou descritiva.

# •	**Variáveis**: São características ou propriedades que podem variar e ser medidas em 
# diferentes unidades. Existem dois tipos principais de variáveis:

#     - Variáveis Quantitativas: Representam quantidades numéricas e podem ser contínuas 
# (como a altura de uma pessoa) ou discretas (como o número de filhos de uma família).
    
#     - Variáveis Qualitativas: Representam atributos ou qualidades que não podem ser quantificadas 
# numericamente. São divididas em duas categorias: nominais (como o gênero de uma pessoa) 
# e ordinais (como a classificação de satisfação do cliente em "ruim", "regular" e "bom").

# •	**População**: É o conjunto completo de todos os elementos que possuem uma característica 
# específica em comum. Por exemplo, se estamos estudando a altura das pessoas no mundo inteiro, 
# a população seria todas as pessoas no planeta.

# •	**Amostra**: É um subconjunto representativo selecionado da população. A amostra é usada para 
# obter informações sobre a população como um todo. A seleção da amostra deve ser feita de forma 
# aleatória e representativa para evitar vieses.

#![title](imagens/PopAmo.jpg)

# **1.3 Objetivos da estatística**

# A estatística tem vários objetivos e aplicações na Ciência de Dados. Alguns dos principais são:

# •	**Descrição**: A estatística descritiva busca resumir e descrever os dados por meio de medidas 
# de tendência central (como média, mediana e moda) e medidas de dispersão (como desvio padrão e variância). 
# Essas medidas fornecem uma visão geral dos dados e de sua variabilidade.

# •	**Inferência**: A estatística inferencial utiliza amostras para fazer inferências e generalizações 
# sobre as populações maiores. Com base nas informações obtidas na amostra, é possível fazer estimativas 
# e testar hipóteses sobre as características da população.


# **1.4 População e amostra**

# Na Ciência de Dados, trabalhamos com amostras de dados para inferir informações sobre uma população maior. Aqui estão algumas etapas envolvidas no processo:

#![title](imagens/PopAmo.jpg)

# 


#Exemplo de criação de um conjunto de dados utilizando a biblioteca NumPy:

import numpy as np

# Criação de um conjunto de dados de altura (variável quantitativa)
altura = np.array([165, 170, 155, 180, 160, 175])
print(altura)
#Exemplo de criação de um conjunto de dados utilizando a biblioteca Pandas:

import pandas as pd

# Criação de um DataFrame com dados de satisfação do cliente (variável qualitativa ordinal)
dados = pd.DataFrame({'Cliente': ['A', 'B', 'C', 'D', 'E'],
                      'Satisfação': ['Bom', 'Ruim', 'Regular', 'Bom', 'Regular']})
# Exibindo o Dataframe
print(dados.head())

#Exemplo de cálculo da média utilizando a biblioteca NumPy:
media = np.mean(altura)
print("A média da altura é:", media)

#Exemplo de seleção de uma amostra aleatória utilizando a biblioteca Pandas:
amostra = dados.sample(n=3)
print("Amostra selecionada:\n", amostra)


