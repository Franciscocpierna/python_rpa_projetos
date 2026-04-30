## <font color='green'>Projeto 7 - Diabetes dos Índios Pima - Parte 05</font>
## <font color='green'>Finalizando o Projeto - Análise Exploratória dos Dados</font>

# Importando os pacotes
# dupla dinâmica
import numpy as np
import pandas as pd
# para plotagem dos gráficos
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
# para geração aleatoria de cores nos gráficos
import random # random library
pallete = ['Accent_r', 'Blues', 'BrBG', 'BrBG_r', 'BuPu', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'OrRd', 'Oranges', 'Paired', 'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdGy_r', 'RdPu', 'Reds', 'autumn', 'cool', 'coolwarm', 'flag', 'flare', 'gist_rainbow', 'hot', 'magma', 'mako', 'plasma', 'prism', 'rainbow', 'rocket', 'seismic', 'spring', 'summer', 'terrain', 'turbo', 'twilight']
# Filtrar as mensagens de alerta (deixar o notebook limpo)
import warnings
warnings.filterwarnings("ignore")

# Criamos uma lista para identificar valores ausentes
lista_labels_valores_ausentes = ["n/a", "na", "NA", "undefined"]

# Carregando o Dataset
dataset = pd.read_csv("dados/dataset_parte4.csv", na_values = lista_labels_valores_ausentes)

print('#'*100)
print(dataset.head())
print('#'*100)
# Como o arquivo salvo não possuia id, ao sarvar o arquivo, o pandas cria uma nova coluna de 
# identificação e ele chama de Unnamed:0 

# Vamos removê-la.
dataset.drop(["Unnamed: 0"], axis = 1, inplace = True)



print('#'*100)
print(dataset.head())
print('#'*100)

print(dataset.shape)

print('#'*100)

print(dataset.info())

print('#'*100)
## Análise Exploratória dos Dados (EDA: Exploratory Data Analysis)
##### Distribuição dos Dados
px.pie(dataset, names="Outcome")

#Podemos ver que no dataset existem 65,1% das pessoas não tem diabetes e 35,9% têm.

##### Gravidez vs Outcome (possuem ou não diabetes)

sns.countplot(x="Pregnancies", hue = "Outcome", data=dataset, palette=random.choice(pallete))
plt.show()

print()
sns.histplot(x="Pregnancies", hue="Outcome", data=dataset, kde=True, palette=random.choice(pallete))
plt.show()
print('#'*100)
#### Pressão Sanguínia (Blood Pressure) vs Outcome (possuem ou não diabetes)
sns.histplot(x="BloodPressure", hue="Outcome", data=dataset, kde=True, palette=random.choice(pallete))
plt.show()
print()
#Podemos ver que os níveis de pressão sanguínea das pessoas com diabetes é um pouco mais alto.
#### Glicose (Glucose) vs Outcome (possuem ou não diabetes)

sns.histplot(x="Glucose", hue="Outcome", data=dataset, kde=True, palette=random.choice(pallete))
plt.show()
print('#'*100)
#Podemos ver que os níveis de glicose das pessoas diabéticas é geralmente alto.
#### "Espessura da Pele" ou dobra cutânea (Skin Thickness) vs Outcome (possuem ou não diabetes)
sns.histplot(x="SkinThickness", hue="Outcome", data=dataset, kde=True, palette=random.choice(pallete))
plt.show()

print()
# Essa grande quantidade central foi resultado da imputação dos dados.
# Podemos ver que pessoas com diabetes tem as dobras cutâneas um pouco maiores (geralmente são pessoas 
# mais obesas).

# Na análise de diabetes, o termo "espessura da pele" se refere à medida da espessura da dobra cutânea 
# (também chamada de dobras de pele ou pregas cutâneas). Essa medida é uma avaliação usada para estimar 
# a quantidade de gordura corporal presente em uma determinada área do corpo.

# A espessura da pele é geralmente medida com um adipômetro, que é um instrumento que mede a dobra da pele 
# e o tecido adiposo subjacente em diferentes pontos do corpo. Essa medida pode ser usada para estimar a 
# porcentagem de gordura corporal, que pode ser um fator importante para avaliar o risco de diabetes e 
# outras condições relacionadas à obesidade.

# No contexto da análise de diabetes, a espessura da pele pode ser considerada um indicador da quantidade 
# de tecido adiposo no corpo, que está frequentemente associada a um risco aumentado de diabetes tipo 2. 
print('#'*100)
#### Idade (Age) vs Outcome (possuem ou não diabetes)
sns.histplot(x="Age", hue="Outcome", data=dataset, kde=True, palette=random.choice(pallete))
plt.show()
print()
# Podemos ver que pessoas mais velhas são mais propensas a ter diabetes.
#### IMC (BMI) vs Outcome (possuem ou não diabetes)
sns.histplot(x="BMI", hue="Outcome", data=dataset, kde=True, palette=random.choice(pallete))
plt.show()

print('#'*100)
#Pessoas com diabetes tem BMI (IMC) mais elevado.
#### Pairplot
sns.pairplot(dataset, hue='Outcome',palette=random.choice(pallete))
plt.show()
print()

print('#'*100)
#### Boxplots
fig, axs = plt.subplots(4, 2, figsize=(20,20))
axs = axs.flatten()
for i in range(len(dataset.columns)-1):
    sns.boxplot(data=dataset, x=dataset.columns[i], ax=axs[i], palette=random.choice(pallete))
    plt.show() 

#### Matriz de Correlação

sns.heatmap(dataset.corr(), linewidths=0.1, vmax=1.0, square=True, cmap='coolwarm', linecolor='white', annot=True).set_title("Mapa de Correlação")
plt.show()

print('#'*100)

# Salvando os dados
dataset.to_csv('dados/dataset_limpo.csv')

