## Noções de Matemática - Álgebra Linear - Parte 3
## 3. Matrizes

# As matrizes são estruturas matemáticas que representam conjuntos de números 
# organizados em linhas e colunas.

# **3.1 Definição e propriedades de matrizes**

# Vamos começar definindo matrizes e explorando algumas de suas propriedades.

import numpy as np

# Definindo matrizes
m1 = np.array([[1, 2, 3], [4, 5, 6]])
m2 = np.array([[7, 8, 9], [10, 11, 12]])

# Imprimindo matrizes
print("Matriz m1:")
print(m1)
print("Matriz m2:")
print(m2)

# Dimensões das matrizes
shape_m1 = m1.shape
shape_m2 = m2.shape
print("Dimensões da matriz m1:", shape_m1)
print("Dimensões da matriz m2:", shape_m2)

# Acessando elementos de uma matriz
element_m1 = m1[0, 1]
element_m2 = m2[1, 2]
print("Elemento na posição (0, 1) da matriz m1:", element_m1)
print("Elemento na posição (1, 2) da matriz m2:", element_m2)