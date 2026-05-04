## Projeto 11 - Boston Housing - Regressão Linear
#### Vamos utilizar o Dataset Boston Housing

# O "Boston Housing Dataset" é derivado de informações coletadas pelo Censo dos Estados Unidos sobre moradias 
# na região de Boston, Massachusetts.:
# Disponível/Fonte (Kaggle): https://www.kaggle.com/datasets/vikrishnan/boston-house-prices
# A seguir estão descritas as colunas do dataset:s

### Descrição dos campos do Dataset:
# - CRIM:Taxa de criminalidade per capita por cidade
# - ZN:Proporção de terreno residencial zoneado para lotes acima de 25.000 pés quadrados
# - INDUS:Proporção de acres de negócios não residenciais por cidade
# - CHAS:Variável dummy do Rio Charles (= 1 se o lote delimita o rio; 0 caso contrário)
# - NOX:Concentração de óxidos nitrosos (partes por 10 milhões)
# - RM:Número médio de cômodos por residência
# - AGE:Proporção de unidades residenciais ocupadas pelo proprietário construídas antes de 1940
# - DIS:Distâncias ponderadas para cinco centros de emprego em Boston
# - RAD:Índice de acessibilidade a rodovias radiais
# - TAX:Imposto sobre a propriedade por extenso por $ 10.000

# - PTRATIO:Proporção aluno-professor por cidade

# - B1000(Bk - 0,63)^2: onde Bk é a proporção de negros por cidade

# - LSTAT:percentual da população de baixa renda

# - TARGET:Valor mediano de casas próprias em $ 1000

# Carregando o Dataset e as bibliotecas que vamos utilizar no projeto...
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from scipy import stats
from sklearn import preprocessing

# para evitar mensagens de alerta/warnings.
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Carregar o módulo de funções para limpeza de dados
from limpeza_dados import *

### Carregando os Dados
# para carregar o dataset vamos definir os nomes das colunas
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
dataset = pd.read_csv('dados\housing.csv', header=None, delimiter=r"\s+", names=column_names)

print(dataset.head(5))

print('#'*100)
### Analisando o Dataset
# Dimensões do dataset
print(np.shape(dataset)) #tanto faz essa linha ou debaixo resta o mesmo
print(dataset.shape)

print('#'*100)
# Vamos ver um resumo dos dados contidos no dataset
print(dataset.describe())

print('#'*100)
# verificando os tipos de dados do dataset
print(dataset.info())

print('#'*100)
# Exibindo o relatório de valores nulos por coluna

print(relatorio_valores_ausentes_por_coluna(dataset))

print('#'*100)
#Desde o início, duas colunas de dados mostram resumos interessantes. Elas são: ZN (proporção de terreno residencial zoneado para 
#lotes acima de 25.000 pés quadrados) com 0 para os percentis 25 e 50. Em segundo lugar, CHAS: variável dummy do Rio Charles 
# (1 se o lote delimita o rio; 0 caso contrário) com 0 para os percentis 25, 50 e 75. Esses resumos são compreensíveis, pois ambas 
# as variáveis são condicionais e categóricas. A primeira hipótese seria que essas colunas podem não ser úteis em tarefas de regressão, 
# como prever MEDV (valor mediano de casas próprias).

#Outro fato interessante sobre o conjunto de dados é o valor máximo de MEDV. A partir da descrição original dos dados, consta: 
# "A variável #14 parece estar censurada em 50,00 (correspondendo a um preço mediano de $ 50.000)". Com base nisso, valores acima de 
# 50,00 podem não ajudar a prever MEDV. Vamos plotar o conjunto de dados e ver tendências/estatísticas interessantes.

## Algumas Visualizações do dataset
fig, axs = plt.subplots(ncols=7, nrows=2, figsize=(20, 10))
index = 0
axs = axs.flatten()
for k,v in dataset.items():
    sns.boxplot(y=k, data=dataset, ax=axs[index])
    index += 1
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
sns.pairplot(dataset, height=2.5)
plt.tight_layout()
plt.show()

#Colunas como CRIM, ZN, RM e B parecem conter outliers. Vamos verificar a porcentagem de outliers em cada coluna.
# Cria um objeto para tratar valores outliers
trata_outlier = ManipuladorDeOutliers(dataset)
# Cria uma lista de colunas float64
lista_colunas = dataset.select_dtypes('float64').columns.tolist()
# Mostra uma visão geral dos outliers
print(trata_outlier.gerar_visao_geral(lista_colunas))
# Substituição dos outliers por margens definidas
trata_outlier.substituir_outliers_por_limites(lista_colunas)
# Mostra uma visão geral dos outliers
print('#'*100)
print(trata_outlier.gerar_visao_geral(lista_colunas))
#Vamos ver como se parecem as distribuições desses recursos e do MEDV.
# Crie uma figura e eixos
fig, axs = plt.subplots(ncols=7, nrows=2, figsize=(20, 10))

# Ajuste a forma dos eixos para um array unidimensional
axs = axs.flatten()

# Percorra as colunas do dataframe
for i, col in enumerate(dataset.columns):
    # Crie um histograma em cada eixo usando histplot
    sns.histplot(dataset[col], ax=axs[i])  # usando histplot

# Ajuste o layout da figura
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)

# Mostre a figura
plt.show()
#O histograma também mostra que as colunas CRIM, ZN e B possuem distribuições altamente assimétricas. 
# Além disso, MEDV parece ter 
# uma distribuição normal (as previsões) e outras colunas parecem ter distribuição normal ou bimodal, 
# exceto CHAS (que é uma variável discreta).

#Agora, vamos plotar a correlação pairwise nos dados.
# plt.figure(figsize=(20, 10))
# sns.heatmap(dataset.corr().abs(),  annot=True)

plt.figure(figsize=(15,10))
cor = dataset.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.PuBu)
plt.show()
# Vamos isolar as características de alta correlação...
cor_target = abs(cor['MEDV']) # valor absoluto de correlação

relevant_features = cor_target[cor_target > 0.35] # isolando as características de alta correlação 

names = [index for index, value in relevant_features.items()] # pegando apenas os nomes das caracteristicas... os que estão em 'items'

names.remove('MEDV') # removendo a variável alvo (MEDV)
print('#'*100)
print(names) #  Mosando a lista das características de alta correlação 
print(len(names))
#A matriz de correlação mostra que TAX e RAD são características altamente correlacionadas. As colunas 'CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT' possuem um valor de correlação acima de 0,35 com MEDV, o que é uma boa indicação para serem usadas como preditoras. Vamos plotar essas colunas em relação ao MEDV.
# Let's scale the columns before plotting them against MEDV
min_max_scaler = preprocessing.MinMaxScaler()
column_sels = ['CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
x = dataset.loc[:,column_sels]
y = dataset['MEDV']
x = pd.DataFrame(data=min_max_scaler.fit_transform(x), columns=column_sels)
fig, axs = plt.subplots(ncols=4, nrows=3, figsize=(20, 15))
index = 0
axs = axs.flatten()
for i, k in enumerate(column_sels):
    sns.regplot(y=y, x=x[k], ax=axs[i])
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
#Com base nessas análises, podemos tentar prever MEDV usando os recursos 'LSTAT', 'INDUS', 'NOX', 'PTRATIO', 'RM', 'TAX', 'DIS' e 'AGE'. 
plt.show()

print()
## Regressão Linear
### Regressão Linear com Scikit-Learn
#Importando as funções necessárias do pacote Scikit-Learn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Dividindo o dataset em teste e treino
column_sels = ['INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'TAX', 'PTRATIO', 'LSTAT']
X = dataset.loc[:,column_sels]
y = dataset['MEDV']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

# Instanciando o modelo de regressão linear
lr = LinearRegression()
lr.fit(X_train, y_train)



print('#'*100)
# Rodando o modelo
predictions = lr.predict(X_test)
# Um exemplo:
print('Valor atual da casa......: ', y_test[0])
print('Valor predito pelo modelo: ', predictions[0])
# Diferença entre o modelo e o valor real
print('$', abs(y_test[0] - predictions[0]))
print()

### Vamos checar a Acurácia do Modelo 

### MSE: Mean Square Error

print('#'*100)
print()

mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
print(mse)

print('#'*100)
print()

#O MSE do modelo está relativamente alto. Pode ser algum problema no split dos dados ou que o modelo de 
# regressão linear não é o modelo mais apropriado para se trabalhar com esse tipo de problema.

### Acurácia do Modelo (%)

print(lr.score(X_test, y_test))
#73,74 % de acurácia de um Modelo de Regressão Linear, não é tão ruim. Todavia, devemos buscar algo um pouco melhor.

#Mas para o primeiro modelo... já está bem legal!!
print('#'*100)
print()


