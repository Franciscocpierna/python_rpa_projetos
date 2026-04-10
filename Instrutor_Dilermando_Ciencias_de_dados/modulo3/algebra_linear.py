

## Noções de Matemática - Álgebra Linear - Parte 1


# **1. Introdução à Álgebra Linear**
# 1.1 O que é álgebra linear e sua importância em ciência de dados
# 1.2 Conceitos básicos: vetores, matrizes e operações fundamentais
# 1.3 Representação gráfica de vetores e matrizes
# 1.4 Resolução de Equações lineares com Matrizes e Vetores

# **2. Vetores**
# 2.1 Definição e propriedades de vetores
# 2.2 Operações com vetores: adição, subtração e multiplicação por escalar
# 2.3 Produto escalar e suas aplicações
# 2.4 Norma de um vetor e distância euclidiana
# 2.5 Vetores ortogonais e produto vetorial

# **3. Matrizes**
# 3.1 Definição e propriedades de matrizes
# 3.2 Operações com matrizes: adição, subtração e multiplicação por escalar
# 3.3 Produto matricial e suas aplicações
# 3.4 Matriz transposta e matriz adjunta
# 3.5 Determinante de uma matriz e sua importância
# 3.6 Matriz inversa e sua aplicação na resolução de sistemas de equações lineares

# **4. Álgebra Linear em Ciência de Dados**
# 4.1 Aplicações de álgebra linear na ciência de dados
# 4.2 Representação de dados usando matrizes
# 4.3 Redução de dimensionalidade e decomposição SVD (Singular Value Decomposition)
# 4.4 Análise de componentes principais (PCA) e suas aplicações
# 4.5 Regressão linear e ajuste de curvas

# **5. Mais Exemplos de Aplicação da Álgebra Linear**
# 5.1 Exemplos práticos de aplicação de álgebra linear em ciência de dados
# 5.2 Implementação de algoritmos e técnicas de álgebra linear em projetos de ciência de dados
# 5.3 Análise exploratória de dados, regressão linear e classificação com base em álgebra linear

# Vamos começar com uma introdução a Álgebra Linear...

## 1. Introdução a Álgebra Linear

# A álgebra linear é um ramo da matemática que estuda vetores, espaços vetoriais e transformações lineares. 
# Ela desempenha um papel fundamental em ciência de dados, fornecendo ferramentas para representar, analisar e 
# resolver problemas complexos. A álgebra linear é usada em uma variedade de áreas, incluindo estatística, aprendizado
# de máquina, processamento de imagens, análise de redes e muito mais.

# **1.1. O que é álgebra linear e sua importância em ciência de dados**

# A álgebra linear trata de operações e estruturas matemáticas relacionadas a vetores e matrizes. Ela permite modelar problemas do mundo real e resolver equações que envolvem múltiplas variáveis. Em ciência de dados, a álgebra linear é amplamente utilizada para:

# - Representar e manipular dados em formato vetorial ou matricial.
# - Realizar operações matriciais para analisar e transformar dados.
# - Resolver sistemas de equações lineares.
# - Reduzir a dimensionalidade dos dados.
# - Realizar ajuste de modelos e aprendizado de máquina.

# A compreensão dos conceitos e técnicas da álgebra linear é essencial para um cientista de dados
# , pois ela fornece uma base sólida para análise e manipulação de dados de alta dimensão.

# **1.2. Conceitos básicos: vetores, matrizes e operações fundamentais**

# Vamos começar com os conceitos básicos de vetores, matrizes e suas operações fundamentais. Utilizaremos 
# a biblioteca NumPy para trabalhar com essas estruturas de dados.


# **Vetores:**

# Um vetor é uma sequência de valores organizados em uma única dimensão. Vamos criar um vetor e 
# realizar algumas operações básicas:

import numpy as np

# Criando um vetor
v = np.array([1, 2, 3])
print("Vetor v:", v)

# Tamanho do vetor
size = len(v)
print("Tamanho do vetor v:", size)

# Acessando elementos do vetor
element = v[0]
print("Primeiro elemento do vetor v:", element)

# Operações com vetores
v2 = np.array([4, 5, 6])
v_sum = v + v2
v_diff = v - v2
v_scalar_mul = 2 * v
print("Soma de vetores v + v2:", v_sum)
print("Subtração de vetores v - v2:", v_diff)
print("Multiplicação escalar de v por 2:", v_scalar_mul)

#**Matrizes:**

# Uma matriz é uma tabela bidimensional de números organizados em linhas e colunas.
#  Vamos criar uma matriz e realizar algumas operações básicas:

import numpy as np

# Criando uma matriz
m = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz m:")
print(m)

# Dimensões da matriz

dim = m.shape
print("Dimensões da matriz m:", dim)

# Acessando elementos da matriz
element = m[0, 1]
print("Elemento na posição (0, 1) da matriz m:", element)

# Operações com matrizes
m2 = np.array([[7, 8, 9], [10, 11, 12]])
m_sum = m + m2
m_diff = m - m2
m_scalar_mul = 2 * m
print("Soma de matrizes m + m2:")
print(m_sum)
print("Subtração de matrizes m - m2:")
print(m_diff)
print("Multiplicação escalar de m por 2:")
print(m_scalar_mul)



# Matriz m:
# [[1 2 3]
#  [4 5 6]]
# Dimensões da matriz m: (2, 3)
# Elemento na posição (0, 1) da matriz m: 2
# Soma de matrizes m + m2:
# [[ 8 10 12]
#  [14 16 18]]
# Subtração de matrizes m - m2:
# [[-6 -6 -6]
#  [-6 -6 -6]]
# Multiplicação escalar de m por 2:
# [[ 2  4  6]
#  [ 8 10 12]]


# **1.3. Representação gráfica de vetores e matrizes**

# Podemos visualizar vetores e matrizes graficamente para ter uma melhor compreensão de suas 
# características e relações. Utilizaremos a biblioteca Matplotlib para criar gráficos.

# **Representação gráfica de vetores:**


import numpy as np
import matplotlib.pyplot as plt

# Vetores
v1 = np.array([1, 2])
v2 = np.array([-2, 1])

# Plotagem dos vetores
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.legend(['v1', 'v2'])
plt.grid()
plt.show()

# Nesse exemplo, criamos dois vetores v1 e v2. Utilizamos a função plt.quiver() do Matplotlib para 
# plotar os vetores no plano cartesiano. Configuramos os rótulos dos eixos, adicionamos uma legenda 
# e exibimos a grade.

# **Representação gráfica de matrizes:**


# Matriz
m = np.array([[1, 2], [3, 4]])

# Plotagem da matriz
plt.imshow(m, cmap='viridis', origin='upper')
plt.colorbar()
plt.xticks([0, 1], ['Coluna 0', 'Coluna 1'])
plt.yticks([0, 1], ['Linha 0', 'Linha 1'])
plt.xlabel('Colunas')
plt.ylabel('Linhas')
plt.title('Representação gráfica da matriz m')
plt.show()

# Nesse exemplo, utilizamos a função plt.imshow() para exibir uma representação gráfica da matriz m.
# Configuramos o mapa de cores com cmap='viridis', adicionamos uma barra de cores com plt.colorbar(), 
# definimos os rótulos dos eixos x e y, e adicionamos um título ao gráfico.]

# **1.4. Resolução de Equações lineares com Matrizes e Vetores**

# A Álgebra Linear é um ramo da matemática que estuda os espaços vetoriais, as transformações lineares e as equações lineares. As equações lineares são aquelas que envolvem somente variáveis com expoentes iguais a 1 e não têm produtos entre variáveis. A forma geral de uma equação linear é:

# a_1 * x_1 + a_2 * x_2 + ... + a_n * x_n = b

# Onde:

# x_1, x_2, ..., x_n são as variáveis desconhecidas.
# a_1, a_2, ..., a_n são os coeficientes das variáveis.

# b é o termo independente.

# A resolução das equações lineares consiste em encontrar os valores das variáveis que satisfazem a equação.

# As equações lineares podem ser resolvidas usando matrizes e vetores. Para isso, podemos representar o sistema de equações lineares na forma matricial.

# Por exemplo, considere o seguinte sistema de equações lineares com duas variáveis x e y:

# 2x + 3y = 8

# 4x - y = 7

# Podemos reescrever esse sistema na forma matricial como:

# | 2  3 |   | x |   | 8 |
# | 4 -1 | * | y | = | 7 |

# Onde:

# A matriz dos coeficientes é a matriz A de dimensão 2x2.
# O vetor das variáveis é o vetor X de dimensão 2x1, contendo as variáveis x e y.
# O vetor dos termos independentes é o vetor B de dimensão 2x1, contendo os valores 8 e 7.

# Agora, para encontrar o vetor X que contém as soluções para as variáveis x e y, podemos utilizar a propriedade das matrizes inversas:

# X = A^(-1) * B

# Onde A^(-1) é a matriz inversa de A.

# **Exemplo de Resolução de Equações Lineares**

# Vamos resolver o sistema de equações lineares do exemplo anterior usando matrizes e vetores.
# Primeiro, vamos criar as matrizes A e B:

# Matriz dos coeficientes
A = np.array([[2, 3], [4, -1]])
print(A)

# Vetor dos termos independentes
B = np.array([[8], [7]])
print(B)

#Agora, podemos calcular a matriz inversa de A e, em seguida, encontrar o vetor X com as soluções:

# Cálculo da matriz inversa de A
A_inv = np.linalg.inv(A)

# Cálculo do vetor X com as soluções
X = A_inv.dot(B)

#Agora, o vetor X contém as soluções para as variáveis x e y. Podemos exibir essas soluções:

print("Soluções:")
print("x =", X[0][0])
print("y =", X[1][0])



# **Visualização Gráfica**

# Para visualizar graficamente a solução do sistema de equações, podemos plotar as retas
#  correspondentes a cada equação linear e o ponto de interseção, que representa a solução.

# Coordenadas das retas
x = np.linspace(-10, 10, 100)
y1 = (8 - 2*x) / 3
y2 = 4*x - 7

# Plot das retas
plt.plot(x, y1, label='2x + 3y = 8')
plt.plot(x, y2, label='4x - y = 7')

# Plot da solução (ponto de interseção)
plt.scatter(X[0][0], X[1][0], color='red', label='Solução')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.title('Visualização Gráfica da Solução')
plt.show()

# O gráfico resultante mostrará as duas retas correspondentes às equações lineares e o 
# ponto de interseção, que representa a solução do sistema.