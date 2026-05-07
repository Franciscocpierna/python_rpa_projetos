
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib as mpl
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression

# para evitar mensagens de alerta/warnings.
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
# Carregar o módulo de funções para limpeza de dados
from limpeza_dados import *

df = pd.read_csv(("dados/Salary_Data.csv"))
print(df.head())
print(df.shape)

print('#'*100)
print(df.info())
print('#'*100)
print(df.describe)


print('#'*100)
#print(df.isna().sum())
# verificando se existe algum valor nulo
calcular_porcentagem_valores_ausentes(df)
figure = px.scatter(data_frame = df, 
                     x="Salary",
                     y="YearsExperience", 
                     size="YearsExperience", 
                     trendline="ols")
figure.show()
# outra forma grafica começa aqui
# Define o tamanho da figura
plt.figure(figsize=(10, 6))

# 1. Cria os pontos (scatter) com tamanhos variados
sns.scatterplot(
    data=df, 
    x="Salary", 
    y="YearsExperience", 
    size="YearsExperience", 
    sizes=(50, 300) # Ajusta o tamanho mínimo e máximo das bolinhas para ficarem visíveis
)

# 2. Adiciona a linha de tendência (OLS - Regressão Linear)
sns.regplot(
    data=df, 
    x="Salary", 
    y="YearsExperience", 
    scatter=False, # Define como False para não desenhar as bolinhas duas vezes
    color="red",   # Linha em vermelho para destacar
    ci=None        # Remove a sombra de margem de erro da linha (opcional)
)

# Adiciona títulos para ficar organizado (opcional)
plt.title("Relação entre Salário e Anos de Experiência")
plt.xlabel("Salário")
plt.ylabel("Anos de Experiência")

# Por fim, desenha o gráfico na tela (ou na janela pop-up, dependendo da sua IDE)
plt.show()

# acaba aqui essa outra forma

print('#'*100)
# verifica se tem pelo menos um dado nulo no dataframe inteiro
#tem_nulos = df.isna().any().any()
#print("O DataFrame tem dados ausentes?", tem_nulos)

# dividindo os dados de treino e teste
X = np.asanyarray(df[["YearsExperience"]])
y = np.asanyarray(df[["Salary"]])
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

# treinando o modelo
model = LinearRegression()
model.fit(Xtrain, ytrain)

# Realizando o teste do modelo
predictions = model.predict(Xtest)

# Verificando a acurácia do modelo
print(f'acurácia = {model.score(Xtest, ytest)}')

a = float(input("Experiência (em Anos): "))
features = np.array([[a]])
sal = model.predict(features)[0][0]
print(f"Prevendo Salário = {sal:.2f}")

print('#'*100)
#total_nulos = df.isna().sum().sum()
#print("Total de dados ausentes:", total_nulos)
#linhas_com_nulos = df[df.isna().any(axis=1)]
#print(f'Visualizar as linhas que contêm dados ausentes: {linhas_com_nulos}')
print()

print('#'*100)
print()


print('#'*100)
print()


print('#'*100)
print()


'''
import plotly.express as px
import os

# Seu código do gráfico aqui...
figure = px.scatter(df, x="Salary", y="YearsExperience", trendline="ols")

# Em vez de figure.show(), faça isso:
nome_arquivo = "meu_grafico.html"
figure.write_html(nome_arquivo)

# Isso abre o arquivo diretamente do seu HD no navegador, sem erro de 127.0.0.1
os.startfile(nome_arquivo)

'''