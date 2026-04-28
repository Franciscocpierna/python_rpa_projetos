# <font color='green'>Projeto 6 - Marketing para Instituições Financeiras - Parte 03</font>
## <font color='green'>Tratamento de Valores Ausentes - A</font>
# Importação dos Pacotes necessários para este projeto
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Carrega o dataset da Parte 2
df = pd.read_csv("dados/bank-full_parte2.csv") 

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
## Tratamento de Valores Ausentes
#Vamos observar a coluna idade (age). Percebemos acima que existem valores nulos.

# Valores ausentes da variável age
print(df.age.isnull().sum())
print('#'*100)
# Calcula o percentual de valores ausentes na variável age
print(df.age.isnull().mean()*100)
print('#'*100)
# Como o percentual é baixo não podemos simplesmente eliminar a coluna. 
# Podemos, sim, eliminar os registros com valores ausentes (essa ação ocasionaria a perda de 21 linhas no dataset) 
# Uma outra opção é fazermos a imputação desses dados ausentes. 
# Para trabalhar essa ausência de dados, vamos fazer a imputação de valores.
# Histograma
df.age.plot(kind = "hist")
plt.title("Histograma da Coluna Idade\n")
plt.show()

print('#'*100)

# Boxplot
sns.boxplot(df.age)
plt.title("Boxplot da Coluna Idade\n")
plt.show()
# Vamos verificar qual é a média de idade.
print(df.age.mean())
print('#'*100)
# Vamos verificar qual é a mediana, valor do meio da distribuição quando os dados estão ordenados.
print(df.age.median())
print('#'*100)
# Vamos verificar qual é a moda, o valor que aparece com mais frequência.
print(df.age.mode())
print('#'*100)
# Ao verificarmos os gráficos, principalmente o boxplot, e depois as medidas (média, mediana e moda), 
# verificamos que se utilizássemos a média ou a mediana poderiamos alterar o padrão dos dados, em virtude 
# de valores "outliers".
# Assim, a medida mais adequada, neste caso em que há poucos valores ausentes, a ser utilizada é a moda! 
# É o que provocará menos impacto no padrão dos dados. 
# Vamos então fazer a imputação dessa medida nos valores ausentes da coluna idade (age).


# Vamos preencher com a moda pois são poucos valores ausentes e assim alteramos muito pouco o padrão nos dados.

print(df.age.fillna("32", inplace = True))

# Agora convertemos para int
df.age = df.age.astype("int")
print(df.age)

# Tipo da variável
print(df.age.dtypes)

print('#'*100)
# Média
print(df.age.mean())

print('#'*100)
# Mediana
print(df.age.median())
print('#'*100)
# Percentual de valores ausentes
print(df.age.isnull().mean()*100)

## Salvando os Dados desta Etapa 3

# Salvando os dados
df.to_csv('dados/bank-full_parte3.csv')