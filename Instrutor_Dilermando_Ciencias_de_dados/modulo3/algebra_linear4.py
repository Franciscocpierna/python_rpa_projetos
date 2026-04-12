## Noções de Matemática - Álgebra Linear - Parte 4
## 4. Álgebra Linear em Ciência de Dados

# A álgebra linear desempenha um papel fundamental na ciência de dados, fornecendo 
# ferramentas para representação, análise e manipulação de dados de alta dimensão.

# **4.1 Aplicações de álgebra linear na ciência de dados**

# A álgebra linear é amplamente utilizada na ciência de dados para diversas aplicações, como:

# •	Representação de dados em formato matricial para facilitar a análise e manipulação.

# •	Redução de dimensionalidade para lidar com dados de alta dimensão.

# •	Análise de componentes principais para identificar padrões e relações entre variáveis.

# •	Ajuste de modelos lineares para realizar previsões e estimativas.

# •	Resolução de sistemas de equações lineares para resolver problemas complexos.

# •	Representação de dados usando matrizes

# Vamos explorar a representação de dados usando matrizes e realizar operações básicas.

import numpy as np

# Dados de exemplo
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Imprimindo matriz de dados
print("Matriz de dados:")
print(data)

# Dimensões da matriz de dados
shape = data.shape
print("Dimensões da matriz de dados:", shape)

# Acessando elementos da matriz de dados
element = data[0, 1]
print("Elemento na posição (0, 1) da matriz de dados:", element)

# Nesse exemplo, criamos uma matriz data que representa um conjunto de dados. Utilizamos o atributo shape
#  para obter as dimensões da matriz e a notação de índice para acessar elementos específicos.

# **4.2 Redução de dimensionalidade e decomposição SVD (Singular Value Decomposition)**

# A redução de dimensionalidade é uma técnica utilizada para reduzir o número de variáveis em 
# um conjunto de dados, mantendo as informações mais relevantes. A decomposição SVD é uma 
# técnica amplamente utilizada para realizar a redução de dimensionalidade.

# Dados de exemplo
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Decomposição SVD (Singular Value Decomposition) --> fatora a matriz em três outras: 
# U - matriz unitária (ortogonal) - vetores singulares à esquerda
# s - matriz diagonal - valores singulares da matriz original
# VT - transposta de uma matriz unitária (ortogonal) - vetores singulares à direita

U, s, VT = np.linalg.svd(data)

# Redução de dimensionalidade
k = 1
reduced_data = U[:, :k] @ np.diag(s[:k]) @ VT[:k, :]

# Imprimindo resultado
print("Dados originais:")
print(data)
print("Dados reduzidos:")
print(reduced_data)

# Explicação do comando:  `reduced_data = U[:, :k] @ np.diag(s[:k]) @ VT[:k, :]`

# 1. **U[:, :k]**:
#    - Aqui, **U** é a matriz de vetores singulares à esquerda. A notação `[:, :k]` significa que 
# estamos selecionando todas as linhas de **U** e apenas as primeiras **k** colunas.
#    - Em termos de redução de dimensionalidade, **U** contém informações sobre como os pontos de 
# dados originais estão relacionados ao espaço de dimensões reduzidas.

# 2. **np.diag(s[:k])**:
#    - **s** é um vetor contendo os valores singulares resultantes da decomposição SVD, ordenados 
# em ordem decrescente.
#    - `[:k]` seleciona apenas os primeiros **k** valores singulares.
#    - `np.diag()` cria uma matriz diagonal com esses valores singulares.
#    - Em suma, esta parte da expressão cria uma matriz diagonal com os primeiros **k** valores singulares.

# 3. **VT[:k, :]**:
#    - **VT** é a matriz de vetores singulares à direita transposta.
#    - A expressão `[:k, :]` seleciona apenas as primeiras **k** linhas de **VT** e todas as colunas.
#    - Em termos de redução de dimensionalidade, **VT** contém informações sobre como os atributos originais estão relacionados ao espaço de dimensões reduzidas.

# 4. **@**:
#    - O operador `@` é o operador de multiplicação de matrizes, introduzido no Python 3.5.

# Assim, a expressão completa `reduced_data = U[:, :k] @ np.diag(s[:k]) @ VT[:k, :]` é essencialmente uma 
# operação de multiplicação de matrizes que reduz a dimensionalidade dos dados originais 
# utilizando os componentes da decomposição SVD. É importante notar que a multiplicação é feita 
# nessa ordem porque **U**, **s**, e **VT** são derivados da decomposição SVD, e a ordem correta de 
# multiplicação é crucial para garantir a correta redução da dimensionalidade e a reconstrução 
# dos dados originais.

# Em seguida, selecionamos um número k de componentes principais e realizamos a redução de dimensionalidade 
# para obter a matriz de dados reduzidos.

# **4.3 Análise de componentes principais (PCA) e suas aplicações**

# A análise de componentes principais (PCA) é uma técnica estatística utilizada para identificar 
# padrões e relações entre variáveis em um conjunto de dados. Ela é amplamente utilizada na redução 
# de dimensionalidade e visualização de dados.

import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Dados de exemplo
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Aplicando PCA
pca = PCA(n_components=2)
transformed_data = pca.fit_transform(data)

# Plotando os dados transformados
plt.scatter(transformed_data[:, 0], transformed_data[:, 1])
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('Análise de Componentes Principais (PCA)')
plt.show()

# Nesse exemplo, utilizamos a biblioteca scikit-learn para aplicar a análise de componentes 
# principais (PCA) nos dados. Em seguida, plotamos os dados transformados em um gráfico de 
# dispersão, onde cada ponto representa uma amostra e as coordenadas são as componentes principais.

# **4.4 Regressão linear e ajuste de curvas**

# A regressão linear é uma técnica estatística utilizada para modelar a relação entre variáveis 
# independentes e dependentes. Ela é amplamente utilizada para realizar previsões e estimativas.

import matplotlib.pyplot as plt

# Dados de exemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Ajuste de curvas
coefficients = np.polyfit(x, y, deg=1)
fit_line = np.polyval(coefficients, x)

# Plotando os dados e a linha ajustada
plt.scatter(x, y)
plt.plot(x, fit_line, color='r')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.title('Ajuste de Curvas - Regressão Linear')
plt.grid(True)
plt.show()

# Nesse exemplo, utilizamos a função np.polyfit() para realizar um ajuste de curvas 
# linear aos dados. Em seguida, utilizamos a função np.polyval() para calcular a linha
# ajustada com base nos coeficientes obtidos. Plotamos os dados originais e a linha ajustada 
# em um gráfico de dispersão.


# Nesse exemplo, utilizamos a função np.linalg.inv() para calcular a matriz inversa de m. 
# Também utilizamos a função np.linalg.solve() para resolver um sistema de equações lineares 
# representado pela matriz m e o vetor b.