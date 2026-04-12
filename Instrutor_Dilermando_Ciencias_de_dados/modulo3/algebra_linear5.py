## Noções de Matemática - Álgebra Linear - Parte 5
## 5. Mais Exemplos de Aplicações da Álgebra Linear

# A álgebra linear desempenha um papel fundamental na ciência de dados, fornecendo ferramentas
#  para representação, análise e manipulação de dados de alta dimensão. Vamos explorar alguns 
# exemplos práticos de aplicação da álgebra linear em projetos de ciência de dados.

# **5.1 Implementação de algoritmos e técnicas de álgebra linear em projetos de ciência de dados**

# Vamos implementar alguns algoritmos e técnicas de álgebra linear comumente utilizados em projetos
#  de ciência de dados.

# **Análise Exploratória de Dados:**

import numpy as np
import pandas as pd

# Carregando dados
data = pd.read_csv('dados.csv')
print(data)
# Análise exploratória de dados
# Exemplo de cálculo da média
media = np.mean(data['coluna1'])  # Corrigido para 'coluna1'
print("Média:", media)

# Exemplo de cálculo da matriz de covariância
covariance_matrix = np.cov(data['coluna1'], data['coluna2'])
print("Matriz de Covariância:")
print(covariance_matrix)

# Nesse exemplo, utilizamos a biblioteca NumPy para realizar uma análise exploratória de dados.
# Calculamos a média de uma coluna do conjunto de dados e a matriz de covariância entre duas colunas.

# **Regressão Linear:**

import numpy as np
from sklearn.linear_model import LinearRegression

# Dados de exemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Ajuste de regressão linear
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)

# Coeficientes da regressão
coeficiente_angular = model.coef_[0]
intercept = model.intercept_

# Imprimindo resultado
print("Coeficiente Angular:", coeficiente_angular)
print("Intercept:", intercept)

# Nesse exemplo, utilizamos a biblioteca scikit-learn para ajustar um modelo de regressão 
# linear aos dados. Calculamos os coeficientes da regressão (coeficiente angular e interceptação) 
# e os imprimimos.

# - Coeficiente Angular: inclinação da linha de regressão e representa a mudança média na variável 
#  dependente (y) conforme o (x) se altera.
# - Intercepto: é o ponto de corte da reta no eixo y (é o valor de y quando x = 0)

# **Classificação:**


from sklearn.linear_model import LogisticRegression

# Dados de exemplo
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])

# Ajuste de modelo de regressão logística
model = LogisticRegression()
model.fit(X, y)

# Previsão
new_data = np.array([[2.5, 3.5]])
prediction = model.predict(new_data)

# Imprimindo resultado
print("Previsão:", prediction)

# Nesse exemplo, utilizamos a biblioteca scikit-learn para ajustar um modelo de regressão logística 
# aos dados. Em seguida, realizamos uma previsão para um novo conjunto de dados e imprimimos o resultado.

# O resultado: Previsão: `[0]` indica que o modelo de regressão logística previu que a nova 
# amostra respresentada por `new_data` pertence à classe `0` com base nos padrões apreendidos 
# ao longo do treinamento.

