# Importando as bibliotecas
import pandas as pd
import numpy as np

# para os gráficos/plotagem
import plotly  #para identificação da versão
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import os
import plotly.express as px
os.environ["OMP_NUM_THREADS"] = "1"
# Importanto o método MinMaxScaler do Sklearn para normalização dos dados
from sklearn.preprocessing import MinMaxScaler

# Importanto o Método KMeans (algoritmo de classificação)
import sklearn  #para identificação da versão
from sklearn.cluster import KMeans

# para evitar mensagens de alerta/warnings.
import warnings
warnings.filterwarnings("ignore")

# Carregar o módulo de funções para limpeza de dados
from limpeza_dados import *
# Mostra todas as colunas
pd.set_option('display.max_columns', None)
# Opcional: Garante que a largura da exibição seja suficiente
#pd.set_option('display.width', 1000)

def mostraGrafico(figure):

        # 2. Define o nome do arquivo que será criado na sua pasta
    nome_arquivo = "grafico_entrega_distancia.html"

    # 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
    figure.write_html(nome_arquivo)

    # 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
    return os.startfile(nome_arquivo)


# Definindo um template
pio.templates.default = "plotly_white"

# Importando o dataset
data = pd.read_csv("dados/userbehaviour.csv")
# mostrando a parte inicial do dataset
print(data.head())


print('#'*20)
# Vamos começar olhando para o tempo de tela mais alto, mais baixo e médio de todos os usuários:
print(f'Average Screen Time = {data["Average Screen Time"].mean()}')
print(f'Highest Screen Time = {data["Average Screen Time"].max()}')
print(f'Lowest Screen Time = {data["Average Screen Time"].min()}')


print()
#Agora vamos dar uma olhada no valor mais alto, mais baixo e na média gasta por todos os usuários:
print(f'Average Spend of the Users = {data["Average Spent on App (INR)"].mean()}')
print(f'Highest Spend of the Users = {data["Average Spent on App (INR)"].max()}')
print(f'Lowest Spend of the Users = {data["Average Spent on App (INR)"].min()}')
print('#'*100)
#Agora vamos dar uma olhada na relação entre a capacidade de gasto e o tempo de tela dos usuários ativos e 
# dos usuários que desinstalaram o aplicativo:

figure = px.scatter(data_frame = data, 
                    x="Average Screen Time",
                    y="Average Spent on App (INR)", 
                    size="Average Spent on App (INR)", 
                    color= "Status",
                    title = "Relationship Between Spending Capacity and Screentime",
                    trendline="ols")
#figure.show()
mostraGrafico(figure)

#Então, isso é ótimo! Os usuários que desinstalaram o aplicativo tinham um tempo médio de tela de menos de 
# 5 minutos por dia, e o valor médio gasto era inferior a 100. Também podemos ver uma relação linear 
# entre o tempo médio de tela e o gasto médio dos usuários que ainda estão usando o aplicativo.

#Agora vamos dar uma olhada na relação entre as avaliações dadas pelos usuários e o tempo médio de tela:

figure = px.scatter(data_frame = data, 
                    x="Average Screen Time",
                    y="Ratings", 
                    size="Ratings", 
                    color= "Status", 
                    title = "Relationship Between Ratings and Screentime",
                    trendline="ols")
#figure.show()
mostraGrafico(figure)
print()

print('#'*100)
# Fazendo o agrupamento dos dados importantes para o modelo.
clustering_data = data[["Average Screen Time", "Left Review", 
                        "Ratings", "Last Visited Minutes", 
                        "Average Spent on App (INR)", 
                        "New Password Request"]]
                        
 # Fazendo a normalização dos dados
for i in clustering_data.columns:
    MinMaxScaler(i)                       

# realizando a classificação.
kmeans = KMeans(n_clusters=3, n_init=10)
clusters = kmeans.fit_predict(clustering_data)
data["Segments"] = clusters

# apresentando os dados.
print(data.head(10))

print()

print('#'*100)
#Agora vamos dar uma olhada no número de segmentos que obtivemos:
print(data["Segments"].value_counts())

# Vamos renomear esse segmentos para melhor entendimento
data["Segments"] = data["Segments"].map({0: "Retained", 1: 
    "Churn", 2: "Needs Attention"})

print()

print('#'*100)
# # Vamos visualizar esses segmentos graficamente
# PLOT = go.Figure()
# for i in list(data["Segments"].unique()):
    

#     PLOT.add_trace(go.Scatter(x = data[data["Segments"]== i]['Last Visited Minutes'],
#                                 y = data[data["Segments"] == i]['Average Spent on App (INR)'],
#                                 mode = 'markers',marker_size = 6, marker_line_width = 1,
#                                 name = str(i)))
# PLOT.update_traces(hovertemplate='Last Visited Minutes: %{x} <br>Average Spent on App (INR): %{y}')

    
# PLOT.update_layout(width = 800, height = 800, autosize = True, showlegend = True,
#                    yaxis_title = 'Average Spent on App (INR)',
#                    xaxis_title = 'Last Visited Minutes',
#                    scene = dict(xaxis=dict(title = 'Last Visited Minutes', titlefont_color = 'black'),
#                                 yaxis=dict(title = 'Average Spent on App (INR)', titlefont_color = 'black')))
# plt.show()
import plotly.graph_objects as go
# 1. Criar a figura
PLOT = go.Figure()

# 2. Adicionar os rastros (traces) por segmento
for i in list(data["Segments"].unique()):
    PLOT.add_trace(go.Scatter(
        x = data[data["Segments"] == i]['Last Visited Minutes'],
        y = data[data["Segments"] == i]['Average Spent on App (INR)'],
        mode = 'markers',
        marker = dict(size=6, line=dict(width=1)),
        name = f"Segmento {i}"
    ))

# 3. Configurar o layout
PLOT.update_layout(
    title = "Segmentação de Usuários",
    width = 800, 
    height = 800, 
    autosize = True, 
    showlegend = True,
    xaxis_title = 'Last Visited Minutes',
    yaxis_title = 'Average Spent on App (INR)',  # Corrigido: era titlpe
    
    # Configuração de fonte para os eixos
    xaxis = dict(title_font=dict(color='black')),
    yaxis = dict(title_font=dict(color='black'))
)

# 4. Ajustar o template do hover
PLOT.update_traces(hovertemplate='Last Visited Minutes: %{x} <br>Average Spent on App (INR): %{y}')

# 5. EXIBIR o gráfico (Use o método do Plotly)
#PLOT.show()

mostraGrafico(PLOT)
print()

#mostraGrafico(figure)

'''

1. Configuração Global (Recomendado)
Adicione estas linhas logo após importar o Pandas. Elas configuram o ambiente para que qualquer print 
mostre todas as colunas e não quebre a linha horizontalmente:

Python
import pandas as pd

# Mostra todas as colunas
pd.set_option('display.max_columns', None)

# Opcional: Garante que a largura da exibição seja suficiente
pd.set_option('display.width', 1000)

print(data.head(10))
2. Usando o to_string()

Se você não quiser mudar as configurações globais e apenas precisar ver o resultado de um print específico, 
use o método to_string():

Python
print(data.head(10).to_string())
Dicas extras para análise de dados:
display.max_rows: Se você quiser ver muitas linhas (ex: None para todas), use pd.set_option('display.max_rows', None).

display.precision: Para controlar quantas casas decimais aparecem (ex: apenas 2), use pd.set_option('display.precision', 2).

No seu caso, como o dataset tem 8 ou 9 colunas, o comando pd.set_option('display.max_columns', None) já será suficiente para remover aqueles pontos no meio do seu resultado e mostrar dados como o "New Password Request" e o "Last Visited Minutes" lado a lado com os outros.

'''