## Projeto 12 - Titanic - Regressão logística 
#### Vamos utilizar o dataset sobre o desastre do Titanic

# Para a explicação desse Método de Resolução de Machine Learning, vamos utilizar um dataset muito famoso, 
# disponível como Competição Initerrupta no Kaggle: **"Titanic - Machine Learning from Disaster"** 
# (fonte: https://www.kaggle.com/competitions/titanic )

# Muito livros e o próprio site do Kaggle, utiliza esse caso como o de entrada no mundo da aprendizagem de 
# máquina.

# ### O Desafio
# O naufrágio do Titanic é um dos naufrágios mais infames da história.

# Em 15 de abril de 1912, durante sua viagem inaugural, o RMS Titanic, considerado amplamente "inafundável", 
# afundou após colidir com um iceberg. Infelizmente, não havia botes salva-vidas suficientes para todos a bordo
# , resultando na morte de 1502 dos 2224 passageiros e tripulantes.

# Embora houvesse um elemento de sorte envolvido na sobrevivência, parece que alguns grupos de pessoas tinham 
# mais probabilidade de sobreviver do que outros.

# Neste desafio, pedimos que você construa um modelo preditivo que responda à pergunta: 
# "que tipos de pessoas tinham mais probabilidade de sobreviver?" usando dados dos passageiros 
# (ou seja, nome, idade, gênero, classe socioeconômica, etc.).

# Para tanto, como é um problema de classificação (sobrevivente ou falecido) podemos utilizar qualquer 
# algoritmo/método de resolução que trabalha com esse tipo de problema. Assim, vamos utilizar a Regressão 
# Logística.

### Descrição do Conjunto de Dados do Titanic

# **Descrição:**
# O conjunto de dados do Titanic é um conjunto de dados clássico usado no campo da ciência de dados e 
# aprendizado de máquina. Ele contém informações sobre os passageiros a bordo do RMS Titanic, que afundou 
# após colidir com um iceberg em sua viagem inaugural em abril de 1912. O conjunto de dados é comumente 
# usado para tarefas de modelagem preditiva, como prever a sobrevivência dos passageiros com base em várias 
# características.

# **Características:**
# - PassengerId: Identificador único para cada passageiro.
# - Survived: Indica se o passageiro sobreviveu (1) ou não (0).
# - Pclass: Classe do bilhete (1ª, 2ª ou 3ª classe).
# - Name: Nome do passageiro.
# - Sex: Gênero do passageiro (masculino ou feminino).
# - Age: Idade do passageiro em anos.
# - SibSp: Número de irmãos/cônjuges a bordo do Titanic.
# - Parch: Número de pais/filhos a bordo do Titanic.
# - Ticket: Número do bilhete.
# - Fare: Tarifa do passageiro.
# - Cabin: Número da cabine.
# - Embarked: Porto de embarque (C = Cherbourg, Q = Queenstown, S = Southampton).

# **Tamanho do Conjunto de Dados:**
# O conjunto de dados geralmente contém informações para cerca de 891 passageiros.

# Vamos importar as bibliotecas e pacotes necessários para toda a nossa análise
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# para evitar mensagens de alerta/warnings.
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Carregar o módulo de funções para limpeza de dados
from limpeza_dados import *


### Carregando o Conjunto de Dados

#Vamos importar o arquivo disponível no site do Kaggle. Lá você encontrará dois: um de treino e outro de 
# teste. Vamos importar o de treino: titanic_train.csv

print('#'*100)
dataset = pd.read_csv('dados/train_titanic.csv')

print(dataset.head())

print('#'*100)
# Dimensões do dataset
print(np.shape(dataset))
print()

print('#'*100)
# Vamos ver um resumo dos dados contidos no dataset
print(dataset.describe())

print('#'*100)

## EDA -  Análise Exploratória dos Dados
### Dados ausentes

# verificando se existe algum valor nulo
print(calcular_porcentagem_valores_ausentes(dataset))

print('#'*100)
# Exibindo o relatório de valores nulos por coluna
relatorio_valores_ausentes_por_coluna(dataset)
print(relatorio_valores_ausentes_por_coluna(dataset))



print('#'*100)
# Maneira simples

print(dataset.isnull().sum())

print('#'*100)
#Essa é a forma de visualização dos dados ausentes que estamos fazendo até agora. Podemos também, 
# utilizando os recursos do Seaborn, mostrar um mapa de calor invertido, mostrando a ausência de valores 
# com uma tonalidade mais clara...

sns.heatmap(dataset.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()
#Conforme estudamos nos módulos de limpeza e preparação dos dados, no caso da idade (Age), podemos utilizar 
# um processo de imputação de idade 
# que estão faltando. Já no caso da identificação da cabine... esse possivelmente teremos que remover 
# (ou também poderiamos trocar esse dado para categórico, informando '1' para numero conhecido da cabine e 
# '0' para desconhecido.

sns.set_style('whitegrid')
sns.countplot(x='Survived',data=dataset,palette='RdBu_r')

#Aqui temos uma noção de que, neste dataset, temos uma quantidade maior de falecidos do que de sobreviventes.

# vamos ver os mesmos dados, divididos por sexo: feminino e masculino.
sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Sex',data=dataset,palette='RdBu_r')

# Agora uma divisão por classe entre mortos e sobreviventes.

# Converter as colunas 'Survived' e 'Pclass' para strings para não dar conflito interno nas classes sns
dataset['Survived'] = dataset['Survived'].astype(str)
dataset['Pclass'] = dataset['Pclass'].astype(str)

# Agora uma divisão por classe entre mortos e sobreviventes.

sns.set_style('whitegrid')
sns.countplot(x='Survived', hue='Pclass', data=dataset, palette='rainbow')

#Os número 1, 2 e 3 representam a 1a., 2a. e 3a. classe.

dataset['Age'].hist(bins=30,color='red',alpha=0.7)
plt.show()

# Vamos dar uma olhada na quantidade de Irmãos ou conjuges a abordo.
sns.countplot(x='SibSp',data=dataset)
plt.show()

#A maioria das pessoas eram solteiras.
dataset['Fare'].hist(color='blue',bins=40,figsize=(8,4))
plt.show()

### Vamos agora Limpar e adequar os dados...

# Os dados da idade faltante: vamos preencher com a média de todos os passageiros (técnica de imputação).
# Entretanto, para melhorar um pouco isso, poderiamos fazer a imputação pela média da idade da classe a qual 
# esse passageiro pertence. Dessa forma, a informação imputada parece ser mais adequada.

# Vamos verificar como está esta distribuição, antes de realizarmos essa imputação...

plt.figure(figsize=(12, 7))
sns.boxplot(x='Pclass',y='Age',data=dataset,palette='winter')
plt.show()

# Com esses boxplots podemos verificar que os passageiros da 1a. classe, ou seja, os mais ricos, são mais 
# velhos. E isto se replica para as demais classes. Portanto, a estratégia se mostra mais coerente... Vamos 
# fazer a imputação.
# Para tanto, vamos criar uma função para tanto. As Medianas das idades são: 1a. classe: 37 anos; 2a. classe: 
# 29 anos e 3a. classe: 24 anos.
def imputar_idade_mediana(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):

        if Pclass == 1:
            return 37

        elif Pclass == 2:
            return 29

        else:
            return 24

    else:
        return Age

#Uma vez definida a função, basta aplicá-la no dataset...     

dataset['Age'] = dataset[['Age','Pclass']].apply(imputar_idade_mediana,axis=1)   
#Agora vamos verificar se os dados foram atualizados e não existe mais valores nulos dem 'Age'...

# Exibindo o relatório de valores nulos por coluna
relatorio_valores_ausentes_por_coluna(dataset)
print('#'*100)
print(relatorio_valores_ausentes_por_coluna(dataset))

print('#'*100)
#Muito bom! Vamos, para finalizar a limpeza... deletar a coluna cabine (Cabin).

dataset.drop('Cabin',axis=1,inplace=True)
# Exibindo o relatório de valores nulos por coluna

print(relatorio_valores_ausentes_por_coluna(dataset))

print('#'*100)
#Por fim, faltam esses dois passageiros que não possuem onde foram embarcados...  Vamos simplesmente deletar 
# esses registros.

dataset.dropna(inplace=True)
# verificando se existe algum valor nulo

print(calcular_porcentagem_valores_ausentes(dataset))

print('#'*100)
# Exibindo o relatório de valores nulos por coluna

print(relatorio_valores_ausentes_por_coluna(dataset))

print('#'*100)
print(dataset.head())


## Ajuste do Dataset
# Vamos converter características categóricas em variáveis dummy usando pandas! 

# REVISANDO:
# **Variáveis dummy**, também conhecidas como variáveis indicadoras ou variáveis binárias, são uma forma de 
# representar variáveis categóricas em modelos estatísticos ou de machine learning. Elas são usadas quando 
# uma variável categórica tem mais do que duas categorias e precisamos representá-la numericamente de uma 
# forma que os modelos possam entender.

# A ideia principal das variáveis dummy é converter cada categoria da variável categórica em uma nova variável 
# binária (0 ou 1), onde 1 indica a presença da categoria e 0 indica a ausência. Isso é necessário porque 
# muitos modelos estatísticos ou algoritmos de machine learning trabalham melhor com variáveis numéricas.

# Caso contrário, nosso algoritmo de Machine Learning não será capaz de aceitar esses recursos diretamente 
# como entradas.

print('#'*100)
print(dataset.info())


print('#'*100)
sex = pd.get_dummies(dataset['Sex'],drop_first=True)  # drop_first=True > Para evitar a multi-colinaridade
embark = pd.get_dummies(dataset['Embarked'],drop_first=True)

dataset.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)

dataset = pd.concat([dataset,sex,embark],axis=1)

print('#'*100)
print(dataset.head())

print('#'*100)

# Muito bom!! Agora nossos dados podem ser utilizados para criar o modelo.
# Vamos utilizar o modelo de Regressão Logística.

## O Modelo de Regressão Logística

# Para reduzir o trabalho, vamos fazer a divisão do próprio conjunto de dados de treino, em treino e teste.
# Existe disponível um dataset apenas para treino... todavia, teríamos que fazer todo esse trabalho de análise. 
# Como o dataset de treino já está pronto, vamos utilizar ele mesmo para as duas tarefas. Mas fique a vontade 
# para fazê-lo utilizando os dois datasets.

### Divisão treino-teste
# aqui vamos fazer a divisão entre treino e teste... a parte de teste ficará com 30% de todo o dataset.
# A forma de divisão será aleatória e será utilizado um código (random_state) para fazer isso. Você pode definir qualquer valor inteiro neste parâmetro.

X_train, X_test, y_train, y_test = train_test_split(dataset.drop('Survived',axis=1), 
                                                    dataset['Survived'], test_size=0.30, 
                                                    random_state=40)
## Fazendo o Treinamento e depois a Predição
# 
# Criando o Modelo de Regressão Logística // fazemos uma determinação do max_iter (número máximo de iterações) 
# para evitar que o modelo não convirja para uma solução apropriada.

logmodel = LogisticRegression(max_iter=1000)

# Treinando o modelo
logmodel.fit(X_train,y_train)

predictions = logmodel.predict(X_test)

# Pronto! Nosso modelo está treinado e com predições. Vamos agora avaliá-lo.
### Avaliação do Modelo

#Podemos verificar a precisão, o recall e a pontuação f1 usando o relatório de classificação!

print(classification_report(y_test,predictions))

### Explicação das Métricas do Modelo de Classificação

# Baseando-se nos resultados fornecidos, podemos explicar as métricas do modelo de classificação da seguinte forma:

# #### Precision (Precisão):
# - **Classe 0 (não sobrevivente)**: A precisão é 0.85. Isso significa que, de todas as previsões feitas pelo modelo que uma pessoa não sobreviveu, 85% estavam corretas.
# - **Classe 1 (sobrevivente)**: A precisão é 0.69. Isso significa que, de todas as previsões feitas pelo modelo que uma pessoa sobreviveu, 69% estavam corretas.

# #### Recall (Revocação ou Sensibilidade):
# - **Classe 0 (não sobrevivente)**: A revocação é 0.79. Isso significa que o modelo identificou corretamente 79% das pessoas que não sobreviveram, de todas as pessoas que realmente não sobreviveram.
# - **Classe 1 (sobrevivente)**: A revocação é 0.77. Isso significa que o modelo identificou corretamente 77% das pessoas que sobreviveram, de todas as pessoas que realmente sobreviveram.

# #### F1-score (F1-Score):
# - **Classe 0 (não sobrevivente)**: O F1-score é 0.82. Isso é uma média harmônica entre a precisão e a revocação, refletindo um equilíbrio entre os dois para a classe 0.
# - **Classe 1 (sobrevivente)**: O F1-score é 0.73. Isso é uma média harmônica entre a precisão e a revocação, refletindo um equilíbrio entre os dois para a classe 1.

# #### Support (Suporte):
# - **Classe 0 (não sobrevivente)**: O suporte é 166. Isso indica que, no conjunto de teste, há 166 exemplos da classe 0.
# - **Classe 1 (sobrevivente)**: O suporte é 101. Isso indica que, no conjunto de teste, há 101 exemplos da classe 1.

# #### Accuracy (Acurácia):
# A acurácia geral do modelo é 0.78. Isso significa que o modelo classificou corretamente 78% dos exemplos no conjunto de teste.

# #### Macro Average (Média Macro):
# - **Precisão Média Macro**: 0.77. É a média das precisões das duas classes.
# - **Revocação Média Macro**: 0.78. É a média das revocações das duas classes.
# - **F1-Score Médio Macro**: 0.77. É a média dos F1-scores das duas classes.

# #### Weighted Average (Média Ponderada):
# - **Precisão Média Ponderada**: 0.79. É a média das precisões ponderada pelo suporte de cada classe.
# - **Revocação Média Ponderada**: 0.78. É a média das revocações ponderada pelo suporte de cada classe.
# - **F1-Score Médio Ponderada**: 0.78. É a média dos F1-scores ponderad classe 0 e 0.73 para a classe 1.

#Portanto, podemos resumir que nosso modelo tem **78% de acurácia**. Não é ruim, mas pode ser melhorada!!
print()


