# <font color='green'>Projeto 6 - Marketing para Instituições Financeiras - Parte 05</font>
## <font color='green'>Tratamento de Valores Ausentes - C</font>

# Importação dos Pacotes necessários para este projeto
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Carrega o dataset
df = pd.read_csv("dados/bank-full_parte4.csv") 

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
#A próxima coluna com valores ausentes que vamos trabalhar é a de salário (salary).
# Valores ausentes na variável
print(df.salary.isnull().sum())
print('#'*100)

# Calcula o percentual de valores ausentes na variável salary
print(df.salary.isnull().mean()*100)

print('#'*100)

# Como o percentual é baixo (menos de 30%) não podemos eliminar a coluna. 
# Assim como nos casos anteriores, aqui também ocorrem as suas possibilidades já informadas: 1) Eliminar os registros com valores
#  ausentes (nesse caso perderíamos 31 linhas no dataset) ou 2) Aplicar imputação nos valores ausentes.

# Além disso... você notou que existem valores iguais a zero nessa coluna? Existe salário igual a zero?
# Pode até existir!!  Portanto, quando se deparar com uma situação semelhante, você tem que confirmar com a área de negócio.
# NÃO PODE EXISTIR ACHISMOS!! NUNCA!!  PARA REALIZARMOS QUALQUER MODIFICAÇÃO NOS DADOS, TEMOS QUE TER CERTEZA!!
print(df.head())

print('#'*100)
# Histograma
df.salary.plot(kind = "hist")
plt.title("Histograma da Variável Salário\n")
plt.show()

# Boxplot
sns.boxplot(df.salary)
plt.title("Boxplot da Variável Salário\n")
plt.show()

# Vamos verificar qual é a média salarial.
print(df.salary.mean())
print('#'*100)
# Vamos verificar qual é a mediana.
print(df.salary.median())
print('#'*100)
# Vamos verificar qual é a moda.
print(df.salary.mode())

print('#'*100)
# Para imputar os valores ausentes da variável salary (salário) com uma medida de tendência central, temos que decidir qual utilizar. 
# Também precisamos tratar os valores iguais a zero. 

# Ao observarmos os dados, percebemos que os mesmos parecem "assimétricos"
# Para dados assimétricos a média não poderia ser utilizada, pois vai mudar o padrão dos dados. A moda também não, pois está muito abaixo da média.

# Portanto, a medida mais indicada para este caso é a utilização da mediana.


# Vamos preencher com a mediana os valores ausentes nesta coluna
print(df.salary.fillna("60000", inplace = True))

print(df.head())
print('#'*100)
# Histograma (vai gerar erro)
# df.salary.plot(kind = "hist")
# plt.title("Histograma da Variável Salário\n")
# plt.show()

# Tipo da variável
print(df.salary.dtypes)

print('#'*100)
# Convertemos para o tipo float
df.salary = df.salary.astype("float")

# Tipo da variável
print(df.salary.dtypes)

# Histograma
df.salary.plot(kind = "hist")
plt.title("Histograma da Variável Salário\n")
plt.show()

# Boxplot
sns.boxplot(df.salary)
plt.title("Boxplot da Variável Salário\n")
plt.show()

# Registros para cada salário
print(df.salary.value_counts())


print('#'*100)
# Replace do zero pela mediana
df['salary'] = df['salary'].replace(0, df['salary'].median())
# Registros para cada salário
print(df.salary.value_counts())

# Histograma
df.salary.plot(kind = "hist")
plt.title("Histograma da Variável Salário\n")
plt.show()

# Boxplot
sns.boxplot(df.salary)
plt.title("Boxplot da Variável Salário\n")
plt.show()
print('#'*100)
# Calcula o percentual de valores ausentes na variável salary
print(df.salary.isnull().mean()*100)


# Temos valores nulos?
print(df.isna().any())


# Salvando os dados
df.to_csv('dados/bank-full_parte5.csv')
