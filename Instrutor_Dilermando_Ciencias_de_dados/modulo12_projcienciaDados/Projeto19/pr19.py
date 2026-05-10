# Importação das bibliotecas/pacotes necessários
# Dupla dinâmica
import pandas as pd
import numpy as np

# dupla dinâmica para exibição dos gráficos
import matplotlib.pyplot as plt
import seaborn as sns

# Para plotagem
import plotly    # esse é apenas para ver a versão
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# Importação da função train_test_split do pacote Sklearn
import sklearn   # esse é apenas para ver a versão
from sklearn.model_selection import train_test_split

# Importanto o Algoritmo Random Forest para fazer a Classificação
from sklearn.ensemble import RandomForestClassifier

# para evitar mensagens de alerta/warnings.
import warnings
warnings.filterwarnings("ignore")

# Carregar o módulo de funções para limpeza de dados
from limpeza_dados import *
#definição de um template de fundo branco para plotagem dos gráficos
pio.templates.default = "plotly_white"

#importação do dataset
data = pd.read_csv("dados/train.csv")

#Exibição das primeiras linhas do dataset
print(data.head())

print('#'*100)
print(data.info())


print()



print('#'*100)
# verificando se existe algum valor nulo
calcular_porcentagem_valores_ausentes(data)
print()

print('#'*100)
### Verificação do balanceamento das informações com relação a coluna objetivo: "Credit_Score"
data["Credit_Score"].value_counts()

import plotly.express as px
import os
#1
fig = px.box(data, 
             x="Occupation",  
             color="Credit_Score", 
             title="Score de Crédito baseado na Ocupação", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
fig.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)


# Não há muita diferença nas pontuações de crédito de todas as ocupações mencionadas nos dados. 

# Agora vamos explorar se a Renda Anual da pessoa impacta sua pontuação de crédito ou não:
#2
fig = px.box(data, 
             x="Credit_Score", 
             y="Annual_Income", 
             color="Credit_Score",
             title="Score de Crédito baseado na Renda Anual", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()

# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
fig.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)

# De acordo com a visualização acima, quanto mais você ganha anualmente, melhor é sua pontuação de crédito. 

# Agora vamos explorar se o salário mensal líquido (in-hand) afeta as pontuações de crédito ou não:
print()
#3
fig = px.box(data, 
             x="Credit_Score", 
             y="Monthly_Inhand_Salary", 
             color="Credit_Score",
             title="Score de Crédito baseado no Salário Líquido Mensal", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
fig.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)

# Assim como a renda anual, quanto mais salário mensal você ganhar, melhor será sua pontuação de crédito. 

# Agora vamos ver se ter mais contas bancárias impacta a pontuação de crédito ou não:
#4
# Verifique se 'data' não está vazio antes de plotar
from time import sleep
sleep(2)
if not data.empty:
    fig = px.box(data, 
                 x="Credit_Score", 
                 y="Num_Bank_Accounts", 
                 color="Credit_Score",
                 title="Score de Crédito baseado no Número de Contas Bancárias", 
                 color_discrete_map={'Poor':'red',
                                     'Standard':'yellow',
                                     'Good':'green'})
    
    fig.update_traces(quartilemethod="exclusive")

    nome_arquivo = "grafico_entrega_distancia.html"
    
    # Salva o arquivo
    fig.write_html(nome_arquivo)
    
    # Mostra o caminho real para você conferir na pasta
    print(f"Arquivo salvo em: {os.path.abspath(nome_arquivo)}")

    # Abre o arquivo
    try:
        os.startfile(nome_arquivo)
    except AttributeError:
        # Caso você esteja no Mac ou Linux, startfile não funciona
        import subprocess
        subprocess.call(['open', nome_arquivo]) 
else:
    print("O DataFrame 'data' está vazio!")


# Manter mais de cinco contas não é bom para ter uma boa pontuação de crédito. 
# Uma pessoa deve ter apenas 2 a 3 contas bancárias. Portanto, ter mais contas bancárias não afeta 
# positivamente a pontuação de crédito. 

# Agora vamos ver o impacto nas pontuações de crédito com base no número de cartões de crédito que você 
# possui:
#5
fig = px.box(data, 
             x="Credit_Score", 
             y="Num_Credit_Card", 
             color="Credit_Score",
             title="Score de Crédito Baseado no Número de Cartões de Crédito", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()

# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
fig.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)

# Assim como o número de contas bancárias, ter mais cartões de crédito não afetará positivamente sua 
# pontuação de crédito. 
# Ter de 3 a 5 cartões de crédito é bom para sua pontuação de crédito. 

# Agora vamos ver o impacto nas pontuações de crédito com base em quanto você paga de juros médios em 
# empréstimos e EMIs (total da prestação mensal de cada pessoa):
#6
fig = px.box(data, 
             x="Credit_Score", 
             y="Interest_Rate", 
             color="Credit_Score",
             title="Score de Crédito Baseado nas Taxas de Juros Médios", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
fig.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)

# Se a taxa média de juros for de 4 a 11%, a pontuação de crédito é boa. 
# Ter uma taxa de juros média de mais de 15% é ruim para sua pontuação de crédito. 

# Agora vamos ver quantos empréstimos você pode tomar por vez para uma boa pontuação de crédito:
#7
fig = px.box(data, 
             x="Credit_Score", 
             y="Num_of_Loan", 
             color="Credit_Score", 
             title="Score de Crédito baseado no número de Emprestimos Tomados por Pessoa",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
fig.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)

# Para ter uma boa pontuação de crédito, você não deve fazer mais de 1 a 3 empréstimos por vez. 
# Ter mais de três empréstimos por vez afetará negativamente sua pontuação de crédito. 

# Agora vamos ver se atrasar os pagamentos na data de vencimento afeta sua pontuação de crédito ou não:
#8
fig = px.box(data, 
             x="Credit_Score", 
             y="Delay_from_due_date", 
             color="Credit_Score",
             title="Score de Crédito baseado na média de números de dias atrasado no pagamentos de Cartão de Crédito", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
fig.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)

# Portanto, atrasar de 4 a 12 pagamentos a partir da data de vencimento não afetará sua pontuação de crédito. 
# Mas atrasar mais de 12 pagamentos a partir da data de vencimento afetará negativamente sua pontuação de crédito. 

# Agora vamos ver se ter mais dívidas afetará a pontuação de crédito ou não:
#9
fig = px.box(data, 
             x="Credit_Score", 
             y="Outstanding_Debt", 
             color="Credit_Score", 
             title="Score de Crédito Baseado em Débitos Pendentes",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
fig.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)

# Uma dívida pendente de $380 – $1150 não afetará sua pontuação de crédito. 
# Mas sempre ter uma dívida de mais de $1338 afetará negativamente sua pontuação de crédito. 

# Agora vamos ver se ter um alto índice de utilização de crédito afetará as pontuações de crédito ou não:

#10
fig = px.box(data, 
             x="Credit_Score", 
             y="Credit_Utilization_Ratio", 
             color="Credit_Score",
             title="Score de Crédito Baseado no Índice de Utilização de Crédito", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()

# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
fig.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)

# Taxa de utilização de crédito significa sua dívida total dividida pelo crédito total disponível.  
# De acordo com a figura acima, sua taxa de utilização de crédito não afeta sua pontuação de crédito. 

# Agora vamos ver como a idade do histórico de crédito de uma pessoa afeta as pontuações de crédito:

#11
fig = px.box(data, 
             x="Credit_Score", 
             y="Credit_History_Age", 
             color="Credit_Score", 
             title="Score de Crédito Baseado na Idade do Histórico de Crédito",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
fig.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)

# Portanto, ter um longo histórico de crédito resulta em melhores pontuações de crédito.

# Agora vamos ver se ter um valor baixo no final do mês afeta a pontuação de crédito ou não:
#12
fig = px.box(data, 
             x="Credit_Score", 
             y="Monthly_Balance", 
             color="Credit_Score", 
             title="Score de Crédito Baseado no Valor Restante no Final do Mês",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
fig.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)



print('#'*100)
### Mapa de Correlação

dados = data.copy()
#dados.corr("spearman")
# Altere a linha 366 de:
# dados.corr("spearman")

# Para:
dados.corr("spearman", numeric_only=True)
# seleciona apenas os dados numéricos
dados_numericos = dados.select_dtypes(include=[np.number])

# Calcula a correlação apenas dos dados numéricos
correl = dados_numericos.corr(method='spearman')

plt.figure(figsize=(21, 21))
sns.heatmap(correl, annot=True)
print(correl)
print()

print('#'*100)

data["Credit_Mix"] = data["Credit_Mix"].map({"Standard": 1, 
                               "Good": 2, 
                               "Bad": 0})

# dividindo os dados 
x = np.array(data[["Annual_Income", "Monthly_Inhand_Salary", 
                   "Num_Bank_Accounts", "Num_Credit_Card", 
                   "Interest_Rate", "Num_of_Loan", 
                   "Delay_from_due_date", "Num_of_Delayed_Payment", 
                   "Credit_Mix", "Outstanding_Debt", 
                   "Credit_History_Age", "Monthly_Balance"]])
y = np.array(data["Credit_Score"])  

#dividindo a base em treinamento e teste. Teste ocupará 33% da base (aleatoriamente)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                    test_size=0.33, 
                                                    random_state=42)

#Instanciando o Classificador do Random Forest no objeto model
model = RandomForestClassifier()

#Realizando a classificação, passando como parâmetro a base de treinamento x e y
model.fit(xtrain, ytrain)

# Realizando o teste do modelo
predictions = model.predict(xtest)

# Verificando a acurácia do modelo
model.score(xtest, ytest)

### Testanto o Modelo

print("***  Prevendo a Pontuação de Crédito (Credit Score)  *** ")
a = float(input("Annual Income: "))
b = float(input("Monthly Inhand Salary: "))
c = float(input("Number of Bank Accounts: "))
d = float(input("Number of Credit cards: "))
e = float(input("Interest rate: "))
f = float(input("Number of Loans: "))
g = float(input("Average number of days delayed by the person: "))
h = float(input("Number of delayed payments: "))
i = input("Credit Mix (Bad: 0, Standard: 1, Good: 3) : ")
j = float(input("Outstanding Debt: "))
k = float(input("Credit History Age: "))
l = float(input("Monthly Balance: "))

features = np.array([[a, b, c, d, e, f, g, h, i, j, k, l]])
pontuacao =  model.predict(features)[0][0]
print("Pontuação de Crédito Prevista = ", pontuacao)

#Previsão realizada... projeto finalizado!
print()

print('#'*100)
print()

print('#'*100)
print()
