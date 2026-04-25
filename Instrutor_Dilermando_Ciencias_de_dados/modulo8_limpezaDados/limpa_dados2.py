
# <font color='green'>Projeto 2 - Escala e Normalização dos dados</font>
## <font color='green'>Instalando os Pacotes e Carregando os Dados</font>


## Instalando e Carregando os Pacotes




# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python : ', python_version())


print('#'*100)

# Para atualizar um pacote, execute o comando abaixo no terminal ou prompt de comando:
# pip install -U nome_pacote

# Importação dos módulos básicos
import numpy as np
import pandas as pd
# Importação para transformação Box-Cox
from scipy import stats
# para fazer a escala de min-max
import mlxtend
from mlxtend.preprocessing import minmax_scaling
# módulos para fazer os gráficos (plotagens)
import seaborn as sns
import matplotlib.pyplot as plt
# módulo para ignorar mensagens de alerta
import warnings
warnings.filterwarnings('ignore')

# Para instalar a versão exata de um pacote, execute o comando abaixo no terminal ou prompt de comando:
# !pip install nome_pacote==versão_desejada

# Depois de instalar ou atualizar o pacote, reinicie o jupyter notebook.

# Instala o pacote watermark. 
# Esse pacote é usado para gravar as versões de outros pacotes usados neste jupyter notebook.
#!pip install -q -U watermark
#!conda install -c conda-forge mlxtend
#pip install -q -U mlxtend

## Carregando os Dados

### Dataset publico: Kickstarter Projects  (mais de 300.000 projetos kickstarter)


# Disponível em: https://www.kaggle.com/code/rtatman/data-cleaning-challenge-scale-and-normalize-data/input?select=ks-projects-201801.csv

# Kickstarter é um site onde as pessoas podem pedir às pessoas que invistam em vários projetos e produtos conceituais.

# Este arquivo estará disponível como recurso dessa aula.

# Criamos uma lista para identificar valores ausentes
lista_labels_valores_ausentes = ["n/a", "na", "undefined"]

# Carrega o dataset "Kickstarter Projets"
dataset = pd.read_csv("dados/ks-projects-201801.csv", na_values = lista_labels_valores_ausentes)

print(dataset.info())

print('#'*100)

# Vamos dar uma olhada nos dados. Nós já fizemos várias vezes com o método head(). Vamos utilizar o 
# método sample, para variar.
# Com ele, temos que informar a quantidade de amostra que queremos.

print(dataset.sample(6))

print('#'*100)
print(dataset.shape)

print('#'*100)
contagem_valores_ausentes = dataset.isnull().sum()
contagem_valores_ausentes[0:20]

# Calculando os totais de celulas e de celulas com valores ausentes (total_nulos)
total_celulas = np.prod(dataset.shape)
total_nulos = contagem_valores_ausentes.sum()
# Calculando o percentual de dados ausentes
print(f"Percentual de Dados ausentes: {(total_nulos/total_celulas):.2%}")
print('#'*100)

## Escala (ou Dimensionamento) e Normalização

# Uma das razões pelas quais é fácil confundir escala (ou dimensionamento) e normalização é porque os termos
# às vezes são usados de forma intercambiável e, para tornar ainda mais confuso, eles são muito semelhantes! 

# Em ambos os casos, você está transformando os valores de variáveis numéricas para que os pontos de dados 
# transformados tenham propriedades úteis específicas. 

# A diferença é que, na escala (ou dimensionamento), você altera o intervalo de seus dados, enquanto na 
# normalização, altera a forma da distribuição de seus dados. 

# ### Escala (ou Dimensionamento) 
# Dimensionar ou mudar a escala, significa que você está transformando seus dados para que caibam em uma 
# escala específica, como 0-100 ou 0-1. Você vai precisar dimensionar os dados quando estiver usando métodos 
# baseados em medidas de pontos de dados distantes, como máquinas de vetor de suporte (SVM) ou k vizinhos mais 
# próximos (KNN). Com esses algoritmos, uma alteração de "1" em qualquer recurso numérico recebe a mesma 
# importância.

# Por exemplo, você pode estar olhando os preços de alguns produtos em ienes e dólares americanos. 
# Um dólar americano vale cerca de 100 ienes, mas se você não dimensionar seus preços, métodos como 
# SVM ou KNN considerarão uma diferença de preço de 1 iene tão importante quanto uma diferença de 1 dólar 
# americano! Isso claramente não se encaixa em nossas intuições do mundo. Com moeda, você pode converter 
# entre moedas. Mas e se você estiver olhando para algo como altura e peso? Não está totalmente claro quantas 
# libras devem ser iguais a uma polegada (ou quantos quilogramas devem ser iguais a um metro).

# Ao dimensionar suas variáveis, você pode ajudar a comparar diferentes variáveis em pé de igualdade. 
# Para ajudar a solidificar a aparência do dimensionamento (escala), vamos trabalhar com alguns dados 
# fictícios (utilizando dados randomizados).


# Geração de 1000 pontos de dados randomicamente utilizando uma distribuição exponencial
dados_originais = np.random.exponential(size = 1000)

# dimensionando os dados min-max entre 0 e 1
dados_escalados = minmax_scaling(dados_originais, columns = [0])

# Fazendo os gráficos de ambos para comparação  (USANDO DISPLOT)
fig, ax=plt.subplots(1,2)
sns.distplot(dados_originais, ax=ax[0])
ax[0].set_title("Dados Originais")
sns.distplot(dados_escalados, ax=ax[1])
ax[1].set_title("Dados Escalados")
plt.show()


print('#'*100)


#Observe que a forma dos dados não muda, mas em vez de variar de 0 a 8, agora varia de 0 a 1.

### Normalização
# O dimensionamento (ou escala) apenas altera o intervalo de seus dados. 

# A normalização é uma *transformação mais radical*. O objetivo da normalização é mudar suas observações 
# para que possam ser descritas como uma **distribuição normal**.

# **Distribuição normal**: também conhecida como "curva de sino", esta é uma distribuição estatística 
# específica em que observações aproximadamente iguais ficam acima e abaixo da média, a média e a mediana 
# são as mesmas e há mais observações mais próximas da média. A distribuição normal também é conhecida como
# *distribuição Gaussiana*.

# Em geral, **você só deseja normalizar seus dados se for usar uma técnica de aprendizado de máquina ou 
# estatística que suponha que seus dados sejam normalmente distribuídos**. Alguns exemplos disso incluem 
# testes T, regressão linear, análise discriminante linear (LDA) e Naive Bayes Gaussiano. 

# (Dica profissional: qualquer método com "Gaussian" no nome provavelmente assume normalidade.)

# O método que estamos usando para normalizar aqui é chamado de *Transformação Box-Cox*. Vamos dar 
# uma olhada rápida em como é a normalização de alguns dados:


# Normalizando os dados exponenciais com boxcox
dados_normalizados = stats.boxcox(dados_originais)[0]


# Fazendo os gráficos de ambos para comparação  (USANDO DISTPLOT)
fig, ax=plt.subplots(1,2)
sns.distplot(dados_originais, ax=ax[0])
ax[0].set_title("Dados Originais")
sns.distplot(dados_normalizados, ax=ax[1])
ax[1].set_title("Dados Normalizados")
plt.show()

#Vamos retornar ao Dataset do Kickstarter...

## Fazendo o Dimensionamento dos dados
# Para ver na prática a aplicação das técnicas de dimensionamento (ou escala) e a normalização, usaremos 
# um conjunto de dados de campanhas do Kickstarter. 

# O Kickstarter é uma comunidade de mais de 10 milhões de pessoas, composta por entusiastas criativos e 
# tecnológicos que ajudam a dar vida a projetos criativos. Mais de $ 3 bilhões de dólares foram contribuídos 
# pelos membros para alimentar projetos criativos. 

# Os projetos podem ser literalmente qualquer coisa - um dispositivo, um jogo, um aplicativo, um filme etc. 
# O Kickstarter funciona com base no tudo ou nada, ou seja, se um projeto não atingir seu objetivo, o 
# proprietário do projeto não recebe nada. Por exemplo, se a meta de um projeto for $ 500, mesmo que seja 
# financiado até $ 499, o projeto não será um sucesso. 

# Neste conjunto de dados, você transformará os valores de variáveis numéricas para que os pontos de dados 
# transformados tenham propriedades úteis específicas.

# Essas técnicas de transformação são conhecidas como dimensionamento ou escalonamento e normalização e uma
# diferença entre essas duas técnicas é que, no escalonamento, você está alterando o intervalo de seus dados
# enquanto na normalização está alterando a forma da distribuição de seus dados. 

# Para entender o resultado de ambas as técnicas, também precisaremos de visualização, portanto, também 
# usaremos algumas bibliotecas de visualização. Vamos entender cada um deles um por um.

# Para dimensionar, primeiro você precisará instalar a biblioteca mlxtend, que é uma biblioteca Python de 
# ferramentas úteis para as tarefas diárias de ciência de dados. Para esta instalação, utilize o comando: 
# *conda install -c conda-forge mlxtend*

# Já fizemos a importação do dataset, agora vamos começar realizando o dimensionamento dos objetivos de cada 
# campanha (quanto dinheiro eles estavam pedindo)....

# Selecionando a coluna usd_goal_real (objetivo real em Dolar americano)
usd_goal = np.array(dataset.usd_goal_real)

# Dimensionando os objetivos entre 0 to 1
dados_escalados = minmax_scaling(usd_goal, columns = [0])


# Mostrando os gráficos dos dados Originais e os dimensinados para comparação (USANDO DISTPLOT)
fig, ax=plt.subplots(1,2)
sns.distplot(usd_goal, ax=ax[0])
ax[0].set_title("Dados Originais")
sns.distplot(dados_escalados, ax=ax[1])
ax[1].set_title("Dados Escalados")

plt.show()

#Você pode ver que o dimensionamento mudou drasticamente as escalas dos gráficos (mas não a forma dos dados: 
# parece que a maioria das campanhas tem metas pequenas, mas algumas têm metas muito grandes)

## Fazendo a Normalização dos dados
#Vamos normalizar a quantia de dinheiro prometida (pledged) para cada campanha.

#Você pode ver que o dimensionamento mudou drasticamente as escalas dos gráficos (mas não a forma dos dados: 
# parece que a maioria das campanhas tem metas pequenas, mas algumas têm metas muito grandes)

# Obtendo o índice de todos os get the index of all positive pledges (Box-Cox only takes postive values)
indice_retorno_positivo = dataset.usd_pledged_real > 0

# Obtendo apenas os retornos positivos (usando seus índices)
retornos_positivos = dataset.usd_pledged_real.loc[indice_retorno_positivo]

# Normalizando os Retornos (c/ Box-Cox)
retornos_normalizados = stats.boxcox(retornos_positivos)[0]

# Fazendo os gráficos comparativos de ambos
fig, ax=plt.subplots(1,2)
sns.distplot(retornos_positivos, ax=ax[0])
ax[0].set_title("Dados Originais")
sns.distplot(retornos_normalizados, ax=ax[1])
ax[1].set_title("Dados Normalizados")

plt.show()
# Ainda não parece perfeito... todavia agora conseguimos verificar que muitas promessas foram pouco estimadas 
# (estimativas baixas). E algumas, muito altas.
# Com o processo de normalização os dados refletem algo mais próximo do normal! 
