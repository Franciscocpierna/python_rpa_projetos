# Vamos importar as biblitecas que vamos precisar para este projeto
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
# importação dos módulos de redes neurais do Keras
import keras
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import tensorflow

# importando funções para preparação dos dados para o modelo e verificação das métricas
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, mean_absolute_percentage_error

# para evitar mensagens de alerta/warnings.
import warnings
warnings.filterwarnings("ignore")

# Carregar o módulo de funções para limpeza de dados
from limpeza_dados import *
# Vamos carregar o dataset
df = pd.read_csv("dados/deliverytime.txt")
print(df.head())


print('#'*100)
# Vamos ver as informações dos campos...

print(df.info())

print('#'*100)
# verificando se existe algum valor nulo
calcular_porcentagem_valores_ausentes(df)
print()
print('#'*100)



# Set the earth's radius (in kilometers)
R = 6371

# Convert degrees to radians
def deg_to_rad(degrees):
    return degrees * (np.pi/180)

# Function to calculate the distance between two points using the haversine formula
def distcalculate(lat1, lon1, lat2, lon2):
    d_lat = deg_to_rad(lat2-lat1)
    d_lon = deg_to_rad(lon2-lon1)
    a = np.sin(d_lat/2)**2 + np.cos(deg_to_rad(lat1)) * np.cos(deg_to_rad(lat2)) * np.sin(d_lon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return R * c
  
# Calculate the distance between each pair of points
df['distance'] = np.nan

for i in range(len(df)):
    df.loc[i, 'distance'] = distcalculate(df.loc[i, 'Restaurant_latitude'], 
                                        df.loc[i, 'Restaurant_longitude'], 
                                        df.loc[i, 'Delivery_location_latitude'], 
                                        df.loc[i, 'Delivery_location_longitude'])
                                        
print('#'*100)
print(df.head())


# figure = px.scatter(data_frame = df, 
#                     x="distance",
#                     y="Time_taken(min)", 
#                     size="Time_taken(min)", 
#                     trendline="ols", 
#                     title = "Relationship Between Distance and Time Taken")
# figure.show()             
#salvando em arquivo
# 

import plotly.express as px
import os

# 1. Configura o gráfico com seus dados de entrega
figure = px.scatter(
    data_frame = df, 
    x="distance",
    y="Time_taken(min)", 
    size="Time_taken(min)", 
    trendline="ols", 
    title = "Relationship Between Distance and Time Taken"
)

# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
figure.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)


#fim salvando em um arquivo no hd


# outra forma grafica começa aqui
# Define o tamanho da figura
plt.figure(figsize=(10, 6))

# 1. Cria os pontos (scatter) com tamanhos variados
sns.scatterplot(
    data=df, 
    x="distance", 
    y="Time_taken(min)", 
    size="Time_taken(min)", 
    #title = "Relationship Between Distance and Time Taken"
    sizes=(50, 300) # Ajusta o tamanho mínimo e máximo das bolinhas para ficarem visíveis
)

# 2. Adiciona a linha de tendência (OLS - Regressão Linear)
sns.regplot(
    data=df, 
    x="distance",
    y="Time_taken(min)",
    scatter=False, # Define como False para não desenhar as bolinhas duas vezes
    color="red",   # Linha em vermelho para destacar
    ci=None        # Remove a sombra de margem de erro da linha (opcional)
)

# Adiciona títulos para ficar organizado (opcional)
plt.title("Relação entre duas ")
plt.xlabel("Distância")
plt.ylabel("tempo levado")

# Por fim, desenha o gráfico na tela (ou na janela pop-up, dependendo da sua IDE)
plt.show()

# acaba aqui essa outra forma
                                       
                                        
print(df.head())



print('#'*100)


figure = px.scatter(data_frame = df, 
                    x="Delivery_person_Age",
                    y="Time_taken(min)", 
                    size="Time_taken(min)", 
                    color = "distance",
                    trendline="ols", 
                    title = "Relationship Between Time Taken and Age")
# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
figure.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)


figure = px.scatter(data_frame = df, 
                    x="Delivery_person_Ratings",
                    y="Time_taken(min)", 
                    size="Time_taken(min)", 
                    color = "distance",
                    trendline="ols", 
                    title = "Relationship Between Time Taken and Ratings")
# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
figure.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)


fig = px.box(df, 
             x="Type_of_vehicle",
             y="Time_taken(min)", 
             color="Type_of_order")

#fig.show()
# 2. Define o nome do arquivo que será criado na sua pasta
nome_arquivo = "grafico_entrega_distancia.html"

# 3. Salva o gráfico como um arquivo HTML (em vez de apenas mostrar)
fig.write_html(nome_arquivo)

# 4. Comando para o Windows abrir o arquivo automaticamente no seu navegador
os.startfile(nome_arquivo)             


print()

print('#'*100)

print()

print('#'*100)

print()

print('#'*100)

print()

