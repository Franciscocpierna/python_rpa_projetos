# Importação dos pacotes básicos
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importação do pacote datetime para trabalhar com dados tipo datetime
import datetime as dt


# para evitar mensagens de alerta/warnings.
import warnings
warnings.filterwarnings("ignore")

# Carregar o módulo de funções para limpeza de dados
from limpeza_dados import *


# Abrindo o dataset
df = pd.read_csv('dados/dailyActivity_merged.csv')

# Exibindo o cabeçalho dos dados

print(df.head(10))

print('#'*100)
# Verificando a quantidade de número de dados únicos no dataset
# verificação pelo Id


print(df['Id'].nunique())

print('#'*100)
# Vamos fazer a filtragem apenas dos dados relevantes o que tornará mais simples e fácil a tarefa de análise dos dados
data = [
    'Id','ActivityDate','TotalSteps','VeryActiveMinutes',
    'FairlyActiveMinutes','LightlyActiveMinutes',
    'SedentaryMinutes','Calories'
]
df = df[data]

print(df.head(10))

print('#'*100)
# Vamos dar mais siginficado para os dados... fazendo a engenharia dos dados:

# Renomeando a coluna 'ActivityDate' em 'Date'

df.rename(columns={'ActivityDate':'Date'},inplace=True)


print(df.head(10))

print('#'*100)
# Vamos criar uma coluna com o total de minutos de todas as atividades realizadas
df['TotalMinutes'] = df['FairlyActiveMinutes'] + df['LightlyActiveMinutes'] + df['SedentaryMinutes']+ df['VeryActiveMinutes']

print(df.head(10))

print('#'*100)
# Criando uma outra coluna do total de horas de todas as atividades
df['TotalHours'] = np.round(df['TotalMinutes']/60)

print(df.head(10))

print('#'*100)
#Verificando os valores, para encontrar nulos e não checados.

print(df.info())
# Mudando a coluna 'Date' para datetime
df['Date'] = pd.to_datetime(df['Date'])
# verificando novamente

print('#'*100)

print(df.info())

print('#'*100)
# Vamos incluir uma nova coluna que contem o dia da semana (DayOfWeek)
df['DayOfWeek'] = df['Date'].dt.day_name()
# Exibindo os dados

print(df.head(10))
# verificando se existe algum valor nulo
calcular_porcentagem_valores_ausentes(df)
print('#'*100)
# Muito bom! Não existem valores nulos no dataset

# Vamos ver agora se existem valores duplicados

print(df.duplicated().sum())
print(df.describe())

# Podemos observar pelas colunas TotalSteps, VeryActiveMinutes, FairlyActiveMinutes e LightlyActiveMinutes 
# que a maioria das pessoas não pratica esportes devido à grande diferença entre o total de passos e os 
# passos ativos.
plt.figure(figsize=(8,4))
plt.hist(df['DayOfWeek'], bins=7, color='lightskyblue', width=0.8)
plt.xticks(rotation = 90)
plt.grid()
plt.title("Freq by day of week")
plt.xlabel('Days Of Week')
plt.ylabel('Frequency')
# O COMANDO ESSENCIAL: parar acertar as margens e aparecer os labels de x e y
plt.tight_layout()
plt.show()
print('#'*100)
#Observamos que as pessoas são muito ativas às terças, quartas e quintas-feiras, então podemos enviar 
#mensagens de motivação para as pessoas nos outros dias.

# Para selecionar apenas os valores numericos
numerical_columns = df.select_dtypes(exclude=object).columns.tolist()
# Vamos mostrar a correlação entre essas colunas de dados numéricos
sns.heatmap(df[numerical_columns].corr())
# O COMANDO ESSENCIAL: parar acertar as margens e aparecer os labels de x e y
plt.tight_layout()
plt.show()

# Vamos então visualizar a relação entre a coluna TotalSteps e a coluna Calories
plt.figure(figsize=(8,6))
plt.scatter(df['TotalSteps'],df['Calories'],c = df['Calories'])
mediansteps =  7405
medianCalory = 2134
plt.axhline(medianCalory, color = 'blue', label = "Median of Calories")
plt.axvline(mediansteps, color = 'red', label = "Median of steps")
plt.title("Calories by steps")
plt.xlabel('Steps')
plt.ylabel('Calories')
plt.legend()
plt.show()


# Vamos visualizar a relação entre a coluna TotalHours com a coluna Calories
plt.figure(figsize=(8,6))
plt.scatter(df['TotalHours'],df['Calories'],c = df['Calories'])
medianHours =  24
medianCalory = 2134
plt.axhline(medianCalory, color = 'blue', label = "Median of Calories")
plt.axvline(medianHours, color = 'red', label = "Median of Hours")
plt.title("Calories by Hours")
plt.xlabel('Hours')
plt.ylabel('Calories')
plt.legend()
plt.show()

#Observamos que existe uma relação fraca entre eles. O que pode explicar isso é o baixo número de minutos 
# ativos.
# Visualizando o percentual de cada coluna com essas outras colunas {VeryActiveMinutes, FairlyActiveMinutes, LightlyActiveMinutes, SedentaryMinutes}
FairlyActiveMinutes = df['FairlyActiveMinutes'].sum()
VeryActiveMinutes = df['VeryActiveMinutes'].sum()
LightlyActiveMinutes = df['LightlyActiveMinutes'].sum()
SedentaryMinutes = df['SedentaryMinutes'].sum()

minuts = [FairlyActiveMinutes,VeryActiveMinutes,LightlyActiveMinutes,SedentaryMinutes]
label = ['FairlyActiveMinutes','VeryActiveMinutes','LightlyActiveMinutes','SedentaryMinutes']

plt.pie(minuts,labels=label,autopct='%1.4f%%',explode=[0,0,0,0.2])
plt.show()

#Podemos dizer que 81 por cento dos usuários utilizam o programa para calcular as calorias queimadas em 
#atividades diárias normais, e também são muito ativos no meio e no final da semana.
print()

print('#'*100)

print()

print('#'*100)

print()