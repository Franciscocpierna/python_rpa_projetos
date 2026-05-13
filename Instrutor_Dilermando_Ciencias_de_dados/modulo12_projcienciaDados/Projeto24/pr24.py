# Importando a dupla dinâmica

import pandas as pd
import numpy as np
from time import sleep

# importando para arquivo temporário
import os
#import plotly.express as px

# Importando o pacote para exibição dos gráficos
import plotly  # apenas para verificação da versão
import plotly.express as px
import plotly.graph_objects as go

# Importando funções de preparação dos dados
import sklearn  # apenas para verificação da versão
from sklearn.model_selection import train_test_split

# Importando o algoritmo de Regressão Linear para criação do modelo de ML
from sklearn.linear_model import LinearRegression

# para evitar mensagens de alerta/warnings.
import warnings
warnings.filterwarnings("ignore")

# Carregar o módulo de funções para limpeza de dados
from limpeza_dados import *

def mostraGrafico(figure):

        # 2. Define o nome do arquivo que será criado na sua pasta
    nome_arquivo = "grafico_entrega_distancia.html"

    # 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
    figure.write_html(nome_arquivo)

    # 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
    return os.startfile(nome_arquivo)

# Carregando o dataset
data = pd.read_csv("dados/advertising.csv")
print(data.head())


print('#'*100)
print(data.info())

print()
print()
print()

# verificando se existe algum valor nulo
calcular_porcentagem_valores_ausentes(data)

print('#'*100)
#Ótimo! Sem valores nulos. Podemos avançar na análise.

### Vamos explorar os dados agora...

# Vamos começar obserando a relação existente entre o montante gasto com propagandas na TV e as unidades 
# vendidas...

print()
figure = px.scatter(data_frame = data, x="Sales",
                    y="TV", size="TV", trendline="ols")
#figure.show()
mostraGrafico(figure)

sleep(2)
#Vamos agora observar a relação existente entre o montante gasto com propagandas em Jornais (Newspaper) e 
# as unidades vendidas...

figure = px.scatter(data_frame = data, x="Sales",
                    y="Newspaper", size="Newspaper", trendline="ols")
mostraGrafico(figure) #figure.show()


# E por fim, vamos observar a relação existente entre o montante gasto com propagandas em Radio e as 
# unidades vendidas...
sleep(2)
figure = px.scatter(data_frame = data, x="Sales",
                    y="Radio", size="Radio", trendline="ols")
mostraGrafico(figure) #figure.show()

print('#'*100)
# De todo o valor gasto em publicidade em várias plataformas, podemos ver pela análise dos gráficos acima, 
# que o valor gasto em publicidade do produto na TV resulta em mais vendas do produto. 

# Agora vamos dar uma olhada na correlação de todas as colunas com a coluna de vendas:

correlation = data.corr()
print(correlation["Sales"].sort_values(ascending=False))


print()
print('#'*100)

#treinar modelo usando regressão linear

y = np.array(data["Sales"])
x = np.array(data.drop(['Sales'], axis=1))

# agora dividindo em treino e teste
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

#Vamos agora treinar o modelo usando o algoritmo de Regressão Linear
model = LinearRegression()
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))
#
#Com uma acurácia de **90%**, o nosso modelo está pronto para fazer previsões...



print()

print('#'*100)
#features = [[TV, Radio, Newspaper]]
features = np.array([[230.1, 37.8, 69.2]])
print(model.predict(features))

# **Conclusão**

# Então, é assim que podemos treinar um modelo de aprendizado de máquina para prever as vendas futuras de 
# um produto. 

# Prever as vendas futuras de um produto ajuda uma empresa a gerenciar os custos de fabricação e publicidade 
# do produto.

print()