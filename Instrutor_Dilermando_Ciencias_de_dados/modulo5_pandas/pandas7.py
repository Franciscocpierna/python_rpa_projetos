
# Pandas - Noções básicas do pacote Pandas - Parte 7

# Construção de Gráficos a partir de DataFrames Pandas
# Além de todos os processos de manipulação de dados, o Pandas também possui algumas funções para exibição 
# de gráficos a partir de dataframes. Vamos ver alguns exemplos...

# Vamos exibir a versão do Scikit-Learn. Ele vai ser utilizado para termos acesso ao dataset Iris
import sklearn
print(sklearn.__version__)
print('#'*50)
#Vamos importar o dataset Iris
from sklearn.datasets import load_iris
data = load_iris()
# Importação do Pandas
import pandas as pd
import matplotlib.pyplot as plt
df_iris = pd.DataFrame(data['data'], columns = data['feature_names'])
df_iris['species'] = data['target']
print(df_iris.head())
print('#'*50)
print(df_iris.shape)
print('#'*50)
print(df_iris.plot())
plt.show()
print('#'*50)
df_iris.plot.scatter(x = 'sepal length (cm)', y = 'sepal width (cm)')
plt.show()

print('#'*50)
#Gráficos mais complexos, com área...
columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']
df_iris[columns].plot.area()
plt.show()

# Calculando a média das colunas agrupadas pela coluna species e criando um gráfico de barras com o resultado
df_iris.groupby('species').mean().plot.bar()
plt.show()

#Contagem das classes da coluna species e plotamos um gráfico de pizza
df_iris.groupby('species').count().plot.pie(y = 'sepal length (cm)')
plt.show()

# Os métodos de plotagem do Pandas são bons, mas limitados.
# No próximo módulo, vamos aprender como trabalhar com o pacote MATPLOTLIB e SEABORN. 
# Com isso, nossos dashboards e visualizações vão ganhar um outro nível!! Até lá!