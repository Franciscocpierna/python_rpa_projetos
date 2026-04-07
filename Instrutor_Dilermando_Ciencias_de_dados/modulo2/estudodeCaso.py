# Importação da "dupla dinânica": Numpy e Pandas
import pandas as pd
import numpy as np

#Importação das bibliotecas gráficas
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import matplotlib.pyplot as plt
import seaborn as sns
#definição de um template de fundo branco para plotagem dos gráficos
pio.templates.default = "plotly_white"
#Importação dos pacotes para criação do modelo
# Importação da função train_test_split do pacote Sklearn
from sklearn.model_selection import train_test_split
# Importanto o Algoritmo Random Forest para fazer a Classificação
from sklearn.ensemble import RandomForestClassifier
# Importando accuracy_score para calcular a Acurácia do modelo
from sklearn.metrics import accuracy_score
#importação do dataset
data = pd.read_csv("dataset/train.csv")
#Exibição das primeiras linhas do dataset 5 default
print(data.head())
print()
print()
data.head()
#5 últimos
#print(data.tail())
#informação sobre tipo
#data.info()
print("#"*50)
### Verificando se existem valores nulos no dataset
#
# A verificação de valores nulos é um dos primeiros passos no processo de análise dos dados. Neste passo verificamos a integridade dos dados e se existem muitos registros e colunas sem informações.
print(data.isnull().sum())
print("#"*50)
# ### Verificação do balanceamento das informações com relação a coluna objetivo: "Credit_Score"
print(data["Credit_Score"].value_counts())
### Conhecendo as relações que existem no dataset
# O conjunto de dados tem muitos recursos que podem treinar um modelo de aprendizado de máquina para classificação de pontuação de crédito. Vamos explorar todos os recursos um por um.
# Vamos começar explorando o recurso de ocupação (occupation) para saber se a ocupação da pessoa afeta a pontuação de crédito:
#pio.renderers.default = "browser"


# print("#"*50)
# fig = px.box(data, 
#              x="Occupation",  
#              color="Credit_Score", 
#              title="Score de Crédito baseado na Ocupação", 
#              color_discrete_map={'Poor':'red',
#                                  'Standard':'yellow',
#                                  'Good':'green'})
# #fig.show()
# pio.show(fig, renderer="browser")
#fig.show(renderer="browser")

# Assim como a renda anual, quanto mais salário mensal você ganhar, melhor será sua pontuação de crédito. 
# Agora vamos ver se ter mais contas bancárias impacta a pontuação de crédito ou não:

# fig = px.box(data, 
#              x="Credit_Score", 
#              y="Num_Bank_Accounts", 
#              color="Credit_Score",
#              title="Score de Crédito baseado no Número de Contas Bancárias", 
#              color_discrete_map={'Poor':'red',
#                                  'Standard':'yellow',
#                                  'Good':'green'})
# fig.update_traces(quartilemethod="exclusive")
# fig.show()

# De acordo com a visualização acima, quanto mais você ganha anualmente, melhor é sua pontuação de crédito. 
# Agora vamos explorar se o salário mensal líquido (in-hand) afeta as pontuações de crédito ou não:

# fig = px.box(data, 
#              x="Credit_Score", 
#              y="Monthly_Inhand_Salary", 
#              color="Credit_Score",
#              title="Score de Crédito baseado no Salário Líquido Mensal", 
#              color_discrete_map={'Poor':'red',
#                                  'Standard':'yellow',
#                                  'Good':'green'})
# fig.update_traces(quartilemethod="exclusive")
# fig.show()

# Assim como a renda anual, quanto mais salário mensal você ganhar, melhor será sua pontuação de crédito. 
# Agora vamos ver se ter mais contas bancárias impacta a pontuação de crédito ou não:

# fig = px.box(data, 
#              x="Credit_Score", 
#              y="Num_Bank_Accounts", 
#              color="Credit_Score",
#              title="Score de Crédito baseado no Número de Contas Bancárias", 
#              color_discrete_map={'Poor':'red',
#                                  'Standard':'yellow',
#                                  'Good':'green'})
# fig.update_traces(quartilemethod="exclusive")
# fig.show()

# Manter mais de cinco contas não é bom para ter uma boa pontuação de crédito. 
# Uma pessoa deve ter apenas 2 a 3 contas bancárias. Portanto, ter mais contas bancárias não afeta positivamente a pontuação de crédito. 

# Agora vamos ver o impacto nas pontuações de crédito com base no número de cartões de crédito que você possui:

# fig = px.box(data, 
#              x="Credit_Score", 
#              y="Num_Credit_Card", 
#              color="Credit_Score",
#              title="Score de Crédito Baseado no Número de Cartões de Crédito", 
#              color_discrete_map={'Poor':'red',
#                                  'Standard':'yellow',
#                                  'Good':'green'})
# fig.update_traces(quartilemethod="exclusive")
# #fig.show()
# #pio.show(fig, renderer="browser")
# fig.show(renderer="browser")

# Assim como o número de contas bancárias, ter mais cartões de crédito não afetará positivamente sua pontuação de crédito. 
# Ter de 3 a 5 cartões de crédito é bom para sua pontuação de crédito. 

# Agora vamos ver o impacto nas pontuações de crédito com base em quanto você paga de juros médios em empréstimos e EMIs (total da prestação mensal de cada pessoa):
# fig = px.box(data, 
#              x="Credit_Score", 
#              y="Interest_Rate", 
#              color="Credit_Score",
#              title="Score de Crédito Baseado nas Taxas de Juros Médios", 
#              color_discrete_map={'Poor':'red',
#                                  'Standard':'yellow',
#                                  'Good':'green'})
# fig.update_traces(quartilemethod="exclusive")
# #fig.show()
# pio.show(fig, renderer="browser")

# Se a taxa média de juros for de 4 a 11%, a pontuação de crédito é boa. 
# Ter uma taxa de juros média de mais de 15% é ruim para sua pontuação de crédito. 

# Agora vamos ver quantos empréstimos você pode tomar por vez para uma boa pontuação de crédito:

fig = px.box(data, 
             x="Credit_Score", 
             y="Num_of_Loan", 
             color="Credit_Score", 
             title="Score de Crédito baseado no número de Emprestimos Tomados por Pessoa",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()
# devido a não carregamento dos gráficos foi criado o arquivo estudodeCaso1.py 
# que grava de um um arquivo temporario no pelo webbrowser sem passar pelo http 
#Isso usa o protocolo 'file://'