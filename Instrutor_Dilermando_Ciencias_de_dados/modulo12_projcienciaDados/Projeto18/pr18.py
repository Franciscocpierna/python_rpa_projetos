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
#fig.show()

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
# Portanto, não há muita diferença entre o tempo levado pelos parceiros de entrega dependendo do veículo 
# que estão dirigindo e do tipo de comida que estão entregando.

# Então, as características que mais contribuem para o tempo de entrega de alimentos com base em 
# nossa análise são:

# - idade do parceiro de entrega
# - avaliações do parceiro de entrega
# - distância entre o restaurante e o local de entrega

# A seguir, vamos treinar um modelo de Machine Learning para previsão do tempo de entrega de alimentos.

# ## Modelo de Previsão do Tempo de Entrega de Alimentos

# Agora vamos treinar um modelo de Machine Learning usando uma rede neural LSTM para a tarefa de previsão 
# do tempo de entrega de alimentos:

#Fazendo a separação dos dados de treino e teste
x = np.array(df[["Delivery_person_Age", 
                   "Delivery_person_Ratings", 
                   "distance"]])
y = np.array(df[["Time_taken(min)"]])
xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                test_size=0.10, 
                                                random_state=42)

# Criando o modelo de rede neural LSTM 
# Inicializa uma rede neural sequencial (uma camada após a outra)
model = Sequential()
# A primeira camada LSTM terá 128 neurônios // input_shape define a forma de entrada de dados. 
# Xtrain.shape representa o número de passos de tempo e o valor 1, representa o número de features
model.add(LSTM(128, return_sequences=True, input_shape= (xtrain.shape[1], 1)))
# Adiciona uma segunda camada com 64 neurônios. A opção False, faz com que essa camada adicione apenas uma única saída com um vetor de 64 dimensões.
model.add(LSTM(64, return_sequences=False))
# Adiciona uma primeira camada densa (totalmente conectada) com 25 unidades.
model.add(Dense(25))
# adiciona uma segunda camada densa com apenas uma unidade (saída)
model.add(Dense(1))
# a linha abaixo imprime um resumo do modelo.
model.summary()

# Fazendo o treinamento do Modelo
# o primeiro parâmetro indica a função de ativação escolhida: Adam (Adaptive Moment Estimation). É eficiente em termos de memória e não precisa
# de muitos ajustes.  //  função de perda (loss) - Erro Médio Quadrático, é uma medida comum para problemas de regressão.
model.compile(optimizer='adam', loss='mean_squared_error')
# batch_size indica a quantidade de amostras de treinamento o modelo processa antes de atualizar os parâmetros.
# epochs indica o número de épocas ou seja a qtd de vezes que o modelo verá todo o conjunto de dados de treinamento.
model.fit(xtrain, ytrain, batch_size=1, epochs=9)

### Acurácia do Modelo

# Avaliar o modelo com os dados de teste
loss = model.evaluate(xtest, ytest)
print(f'Loss (Erro Quadrático Médio): {loss}')

# Fazer previsões com os dados de teste
predictions = model.predict(xtest)

# Calcular métricas adicionais
mae = mean_absolute_error(ytest, predictions)
r2 = r2_score(ytest, predictions)
print(f'Erro Médio Absoluto (MAE): {mae}')
print(f'R² Score: {r2}')

# Calcular a acurácia do modelo
# Calcular MAPE
mape = mean_absolute_percentage_error(ytest, predictions)
# Calcular acurácia percentual
accuracy = 100 - mape * 100
print(f'Acurácia: {accuracy:.2f}%')

print()
### Testando o Modelo

print("Predição do Tempo de Entrega de Alimentos")
a = int(input("Idade do Entregador: "))
b = float(input("Avaliação das Entregas Anteriores (1-5): "))
c = int(input("Distância Total: "))

features = np.array([[a, b, c]])
tempo = model.predict(features)[0][0]
print(f"Previsão do Tempo de Entrega: {tempo:.2f} minutos")

#Então, assim é como você pode usar Machine Learning para a tarefa de previsão do tempo de entrega de 
# alimentos.
print('#'*100)

print()

print('#'*100)

print()

