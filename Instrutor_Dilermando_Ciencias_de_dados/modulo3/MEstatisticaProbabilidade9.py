## Noções de Matemática - Estatística e Probabilidade - Parte 9

## 9. Regressão Linear

# **9.1 Análise de Regressão Simples**

# A análise de regressão simples é uma técnica estatística usada para modelar a relação entre uma
# variável independente (preditora) e uma variável dependente (resposta) por meio de uma linha reta.

# ![title](imagens/regressao.jpg)
 
# No gráfico acima, temos a representação do conjunto de dados indicados pelos pontos em vermelho. 
# Cada ponto indica um ponto de dado. A reta na cor azul representa a reta de regressão de todos os 
# pontos de dados. Ou seja, é a reta criada por uma função f(x) que representa o comportamento médio 
# de todos os pontos de dados.

# Quando analisamos um conjunto de dados específicos, podemos utilizar a regressão linear para
#  modelar uma função que representa um comportamento médio dos pontos de dados. Esta função pode 
# ser utilizada para “prever” um próximo valor de entrada de dados.

# Portanto, a regressão linear é amplamente utilizada em Ciência de Dados para fazer previsões 
# e entender a relação entre variáveis. Aqui estão os passos para realizar uma análise 
# de regressão simples:

# •	**Definir as variáveis**: Identifique a variável independente (x) e a variável dependente (y) 
# que deseja relacionar.

# •	**Visualizar os dados**: Plote os dados em um gráfico de dispersão para entender a relação 
# entre as variáveis.

# •	**Ajustar o modelo**: Ajuste o modelo de regressão linear simples aos dados. Isso envolve
#  encontrar os coeficientes da reta que melhor se ajustam aos dados.

# •	**Interpretar os coeficientes**: Interprete os coeficientes da regressão, que representam 
# o intercepto (valor quando x=0) e a inclinação (mudança na resposta para uma unidade de mudança em x).

# •	**Avaliar a qualidade do modelo**: Avalie a qualidade do modelo por meio de métricas como 
# o erro médio quadrático (RMSE) e o coeficiente de determinação (R²).

# •	**Fazer previsões**: Use o modelo ajustado para fazer previsões para novos valores de x.

# Análise de Regressão Simples

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dados de exemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

# Visualizar os dados
plt.scatter(x, y)
plt.xlabel('Variável Independente (x)')
plt.ylabel('Variável Dependente (y)')
plt.title('Análise de Regressão Simples')
plt.show()

# Ajustar o modelo de regressão linear
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)

# Coeficientes do modelo
intercept = model.intercept_
slope = model.coef_[0]

print("Intercepto:", intercept)
print("Inclinação:", slope)


# **9.2 Coeficiente de Correlação**

# O coeficiente de correlação é uma medida estatística que quantifica a força e a direção da relação linear entre duas variáveis.
# Ele varia de -1 a 1, onde valores próximos de -1 indicam uma correlação negativa forte, valores próximos de 1 indicam uma correlação 
# positiva forte e valores próximos de 0 indicam uma correlação fraca ou inexistente. O coeficiente de correlação pode ser calculado 
# usando a fórmula matemática ou utilizando funções estatísticas disponíveis em bibliotecas como NumPy ou Pandas.

# Coeficiente de Correlação

import numpy as np
from scipy.stats import pearsonr

# Dados de exemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

# Calcular o coeficiente de correlação
correlation_coef, p_value = pearsonr(x, y)

print("Coeficiente de Correlação:", correlation_coef)


# Dado o conceito de coeficiente de correlação, um recurso importantíssimo e muito utilizado na área de Ciência de Dados 
# é o Mapa de Correlação. Nesse mapa, observa-se a correlação entre variáveis. Os pontos mais escuros representam uma correlação 
# mais próxima de 1 (forte correlação) e os pontos mais claros, correlação próxima a -1 (baixa correlação).

# O código abaixo mostra um exemplo de utilização do mapa de correlação. Certifique-se de que tanto o Pandas, quanto o Seaborn
#  estejam instalados.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Criando um DataFrame com dados fictícios
np.random.seed(42)
data = {
    'Variavel1': np.random.rand(100),
    'Variavel2': np.random.rand(100),
    'Variavel3': np.random.rand(100),
    'Variavel4': np.random.rand(100),
    'Variavel5': np.random.rand(100)
}
df = pd.DataFrame(data)

# Calculando a matriz de correlação
correlation_matrix = df.corr()
print(correlation_matrix)

# Criando o mapa de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center = 0, square = True)
plt.title('Mapa de Correlação')
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
print("Versão do pandas:", pd.__version__)
print("Versão do numpy:", np.__version__)
print("Versão do seaborn:", sns.__version__)
print("Versão do matplotlib:", matplotlib.__version__)
import notebook
print("notebook = ", notebook.__version__)
#print(conda --version)
#print(python --version)

# **9.3 Coeficiente de Determinação**

# O coeficiente de determinação, também conhecido como R², é uma medida estatística que representa a proporção da variabilidade
# da variável dependente (resposta) que pode ser explicada pelas variáveis independentes (preditoras) em um modelo de regressão.
#  O R² varia de 0 a 1, onde valores próximos de 1 indicam que o modelo explica uma grande parte da variabilidade dos dados e 
# valores próximos de 0 indicam que o modelo não explica bem os dados. O coeficiente de determinação pode ser calculado 
# como o quadrado do coeficiente de correlação entre as variáveis.


import numpy as np
from scipy.stats import linregress

# Dados de exemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

# Calcular o coeficiente de determinação
slope, intercept, r_value, p_value, std_err = linregress(x, y)
r_squared = r_value**2

print("Coeficiente de Determinação (R²):", r_squared)

# Coeficiente de Determinação