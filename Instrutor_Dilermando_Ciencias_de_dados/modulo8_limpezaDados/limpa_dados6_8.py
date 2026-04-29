# <font color='green'>Projeto 6 - Marketing para Instituições Financeiras - Parte 08</font>
## <font color='green'>Algumas análises e finalização</font>

# Importação dos Pacotes necessários para este projeto
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
# Carrega o dataset
df = pd.read_csv("dados/bank-full_final.csv") 
print(df.shape)

print('#'*100)
print(df.head())


print('#'*100)
# Como removemos o id, ao sarvar o arquivo, o pandas cria uma nova coluna de identificação e ele chama de Unnamed:0 
# Vamos removê-la.
df.drop(["Unnamed: 0"], axis = 1, inplace = True)
print(df.head())



print('#'*100)
print(df.info())
print('#'*100)
# Temos valores nulos?
print(df.isna().any())

print('#'*100)
# Temos valores nulos?
print(df.isna().sum())
print('#'*100)
## Análise dos Dados
# Alguma análises que podem ser feitas e entregues para a área de negócio ou para a equipe que fará o 
# "data science", tentando reconhecer algum padrão ou mesmo estabelecer um modelo de possível previsão, 
# no caso, de opção ou não pela campanha de marketing.

### Análise Univariada
# A **análise univariada** compreende *explicar a distribuição de uma única variável*, incluindo sua medida 
# central (média, mediana e a moda) e sua dispersão (incluindo a diferença entre o maior e menor 
# valor da amostragem e quantis do conjunto de dados, além da variância e desvio padrão).

# Vamos analisar três colunas (variáveis): estado civil (marital), profissão (job) e nível educacional 
# (education)

# Análise da coluna/variável estado civil (marital)
print(df.marital.value_counts(normalize = True))
# Agora no formato gráfico (gráfico de barras)
df.marital.value_counts(normalize = True).plot(kind = "barh")
plt.title("Distribuição da variável estado civil\n")
plt.legend()
plt.show()
print('#'*100)
# Análise da coluna/variável profissão (job)
print(df.job.value_counts(normalize = True))
# Agora no formato gráfico (gráfico de barras)
plt.figure(figsize = (10,6))
df.job.value_counts(normalize = True).plot(kind = "barh")
plt.title("Distribuição da variável Profissão\n", fontdict = {'fontsize': 20, 'fontweight' : 5, 'color' : 'Green'})
plt.legend()
plt.show()


print('#'*100)

# Análise da coluna/variável nível educacional (education)
print(df.education.value_counts(normalize = True))

# Agora no formato gráfico (gráfico de pizza)
plt.figure(figsize = (10,6))
df.education.value_counts(normalize = True).plot(kind = "pie")
plt.title("Distribuição da variável Nível Educacional\n", fontdict = {'fontsize': 20, 'fontweight' : 5, 'color' : 'Green'})
plt.legend()
plt.legend(bbox_to_anchor=(1.31,0.4))
plt.show()
print('#'*100)
#### Análise Multivariada
# A **Análise Multivariada** refere-se a um conjunto de métodos estatísticos que permitem analisar 
# simultaneamente várias variáveis medidas em cada elemento amostral. Esses métodos têm como objetivo 
# simplificar ou facilitar a interpretação do fenômeno que está sendo estudado, identificando os fatores 
# e as relações entre eles. Alguns exemplos de métodos de análise multivariada são: análise de correspondência
# ou matriz de correspondência, análise de componentes principais, análise fatorial, análise de cluster, 
# análise de regressão múltipla e modelagem de equações estruturais.
# Por exemplo... será que existe alguma correlação entre idade, saldo em conta corrente e salário?

# Calcula a correlação
res = df[["salary", "balance", "age"]].corr()

# Mapa de Correlação
plt.figure(figsize = (10,5))
sns.heatmap(res, annot = True, cmap = "Reds")
plt.title("Mapa de Correlação\n", fontdict = {'fontsize': 20, 'fontweight' : 5, 'color' : 'Green'})
plt.show()
print('#'*100)
#Uma outra análise multivariada que pode ser feita é identificar se existe alguma correlação entre o salário 
# e a opção por aderir a campanha de marketing. Será que as pessoas que ganham mais foram mais propensas a 
# dizer "sim"?
# Agrupa o salário pela variável alvo (target) e calcula a média
print(df.groupby(by = ["target"])["salary"].mean())

print('#'*100)
# Agrupa o salário pela variável resposta e calcula a mediana
print(df.groupby(by = ["target"])["salary"].median())
print('#'*100)

# Boxplot
plt.figure(figsize = (10,5))
sns.boxplot(x=df["target"], y=df["salary"])
plt.title("Salário x Target\n", fontdict = {'fontsize': 20, 'fontweight' : 5, 'color' : 'Green'})
plt.show()
print('#'*100)
print('#'*100)


