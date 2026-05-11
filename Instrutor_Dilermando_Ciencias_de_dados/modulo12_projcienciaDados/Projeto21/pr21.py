
# Importando os básicos
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Importanto metodos para pre-processamento e normalização
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Vamos realizar o projeto analisando 6 algoritmos:
from sklearn.linear_model import LinearRegression
from sklearn. linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
import xgboost

# Importando métodos para verificação de metricas
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn import metrics 

# para evitar mensagens de alerta/warnings.
import warnings
warnings.filterwarnings("ignore")

# Carregar o módulo de funções para limpeza de dados
from limpeza_dados import *

# Importantando o dataset
data_df = pd.read_csv("dados/diamonds.csv")

print(data_df.head())
print('#'*100)
# Checando para valores nulos e as variaveis categóricas do dataset
print(data_df.info())
print()

print('#'*100)
# verificando se existe algum valor nulo
calcular_porcentagem_valores_ausentes(data_df)

print()

print('#'*100)

# Valores duplicados

print(data_df.duplicated().sum())


print('#'*100)

data_df.drop_duplicates(inplace=True)
print(data_df)


plt.figure(figsize=(10, 8))
cols = ["#6495ED", "#FFA07A", "#20B2AA", "#9370DB", "#00CED1"]  # Different colors
ax = sns.violinplot(x="cut", y="price", data=data_df, palette=cols, scale="count")
ax.set_title("Diamond Cut for Price", color="#774571", fontsize=20)
ax.set_ylabel("Price", color="#4e4c39", fontsize=15)
ax.set_xlabel("Cut", color="#4e4c39", fontsize=15)
plt.show() 


plt.figure(figsize=(12, 8))  # Set the figure size
cols = ["#6495ED", "#FFA07A", "#20B2AA", "#9370DB", "#00CED1"]  # Different colors
ax = sns.violinplot(x="color", y="price", data=data_df, palette=cols, scale="count")
ax.set_title("Diamond Colors for Price", color="#774571", fontsize=20)
plt.show()


plt.figure(figsize=(13, 8))  # Set the figure size
cols = ["#6495ED", "#FFA07A", "#20B2AA", "#9370DB", "#00CED1"]  # Different colors
ax = sns.violinplot(x="clarity", y="price", data=data_df, palette=cols, scale="count")
ax.set_title("Diamond Clarity for Price", color="#774571", fontsize=20)
ax.set_ylabel("Price", color="#4e4c39", fontsize=15)
ax.set_xlabel("Clarity", color="#4e4c39", fontsize=15)
plt.show()

lm = sns.lmplot(x="price", y="y", data=data_df, scatter_kws={"color": "#BC8F8F"}, line_kws={"color": "#8B4513"})
plt.title("Line Plot on Price vs 'y'", color="#774571", fontsize = 20)
plt.show()


lm = sns.lmplot(x="price", y="z", data=data_df, scatter_kws={"color": "#BC8F8F"}, line_kws={"color": "#8B4513"})
plt.title("Line Plot on Price vs 'z'", color="#774571", fontsize = 20)
plt.show()

lm = sns.lmplot(x="price", y="depth", data=data_df, scatter_kws={"color": "#BC8F8F"}, line_kws={"color": "#8B4513"})
plt.title("Line Plot on Price vs 'depth'", color="#774571", fontsize = 20)
plt.show()

lm = sns.lmplot(x="price", y="table", data=data_df, scatter_kws={"color": "#BC8F8F"}, line_kws={"color": "#8B4513"})
plt.title("Line Plot on Price vs 'Table'", color="#774571", fontsize = 20)
plt.show()


print('#'*100)
# Removendo a característica (feature) "Unnamed"
data_df = data_df.drop(["Unnamed: 0"], axis=1)

print(data_df)

print('#'*100)
# Removendo os pontos de dados (registros) que tenham o valor mínimo de 0 em quaisquer características (campos) x, y or z
data_df = data_df.drop(data_df[data_df["x"]==0].index)
data_df = data_df.drop(data_df[data_df["y"]==0].index)
data_df = data_df.drop(data_df[data_df["z"]==0].index)
data_df.shape
print(data_df.shape)

print('#'*100)
## Removendo os outliers (valores extremos) definindo parâmetros apropriados
data_df = data_df[(data_df["depth"]<75)&(data_df["depth"]>45)]
data_df = data_df[(data_df["table"]<80)&(data_df["table"]>40)]
data_df = data_df[(data_df["x"]<40)]
data_df = data_df[(data_df["y"]<40)]
data_df = data_df[(data_df["z"]<40)&(data_df["z"]>2)]

print(data_df.shape)



print('#'*100)
# Fazendo uma cópia do dataset original 
data1 = data_df.copy()

# Aplicando "Label encoder" para as colunas com dados categórios
columns = ['cut','color','clarity']
label_encoder = LabelEncoder()
for col in columns:
    data1[col] = label_encoder.fit_transform(data1[col])

print(data1.describe())

print('#'*100)
## Dividindo os dados
# Definindo as variáveis dependentes e independentes
X= data1.drop(["price"],axis =1)
y= data1["price"]
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=42)

# Regressão Linear
pipeline_lr=Pipeline([("scalar1",StandardScaler()),
                     ("lr",LinearRegression())])

# Lasso
pipeline_lasso=Pipeline([("scalar2", StandardScaler()),
                      ("lasso",Lasso())])

# Tabela de Decisão
pipeline_dt=Pipeline([("scalar3",StandardScaler()),
                     ("dt",DecisionTreeRegressor())])
# Random Forest
pipeline_rf=Pipeline([("scalar4",StandardScaler()),
                     ("rf",RandomForestRegressor())])

# KNN
pipeline_kn=Pipeline([("scalar5",StandardScaler()),
                     ("kn",KNeighborsRegressor())])

# XGBoost
pipeline_xgb=Pipeline([("scalar6",StandardScaler()),
                     ("xgb",XGBRegressor())])

# Criando uma lista de todos os pipelines dos algoritmos
# List of all the pipelines
pipelines = [pipeline_lr, pipeline_lasso, pipeline_dt, pipeline_rf, pipeline_kn, pipeline_xgb]

# Criando um dicionario dos pipelines e tipos de modelos para referência
pipeline_dict = {0: "LinearRegression", 1: "Lasso", 2: "DecisionTree", 3: "RandomForest",4: "KNeighbors", 5: "XGBRegressor"}

# Ajustando (fit) os pipelines 
# Vamos usar o método "fit" para estimar os parâmetros dos modelos em cada pipeline com base nos dados de treinamento fornecidos
for pipe in pipelines:
    pipe.fit(X_train, y_train)

# Observando os resultados para cada pipeline..
# O resultado mostrará a média do erro quadrático médio (RMSE) negativo para cada modelo / algoritmo após a validação cruzada em 12 dobras (folds).
# O RMSE é uma medida comum de precisão para modelos de regressão, onde valores menores indicam modelos mais precisos.
cv_results_rms = []
for i, model in enumerate(pipelines):
    cv_score = cross_val_score(model, X_train,y_train,scoring="neg_root_mean_squared_error", cv=12)
    cv_results_rms.append(cv_score)
    print("%s: %f " % (pipeline_dict[i], -1 * cv_score.mean()))


## Previsão do modelo nos dados de teste com XGBClassifier
#Que nos deu o menor RMSE
pred = pipeline_xgb.predict(X_test)
print("R^2:",metrics.r2_score(y_test, pred))
print("Adjusted R^2:",1 - (1-metrics.r2_score(y_test, pred))*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1))    
#Portanto... uma acurácia de mais de 98%
print()

print('#'*100)

print()