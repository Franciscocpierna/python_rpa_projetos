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

# Nesse exemplo, criamos duas matrizes m1 e m2. Utilizamos o atributo shape para 
# obter as dimensões das matrizes e a notação de índice para acessar elementos específicos.

# **3.2 Operações com matrizes: adição, subtração e multiplicação por escalar**

# Vamos explorar as operações básicas com matrizes: adição, subtração e multiplicação por escalar.



# Matrizes
m1 = np.array([[1, 2, 3], [4, 5, 6]])
m2 = np.array([[7, 8, 9], [10, 11, 12]])

# Operações com matrizes
m_sum = m1 + m2
m_diff = m1 - m2
m_scalar_mul = 2 * m1

# Imprimindo resultados
print("Soma de matrizes m1 + m2:")
print(m_sum)
print("Subtração de matrizes m1 - m2:")
print(m_diff)
print("Multiplicação escalar de m1 por 2:")
print(m_scalar_mul)

# Nesse exemplo, realizamos a adição de m1 e m2, a subtração de m1 por m2 e a multiplicação de 
# m1 por um escalar de 2.

# **3.3 Produto matricial e suas aplicações**

# O produto matricial (também conhecido como multiplicação de matrizes) é uma operação que combina 
# duas matrizes, produzindo uma nova matriz.


# Matrizes
m1 = np.array([[1, 2, 3], [4, 5, 6]])
m2 = np.array([[7, 8], [9, 10], [11, 12]])

# Produto matricial
m_product = np.dot(m1, m2)

# Imprimindo resultado
print("Produto matricial entre m1 e m2:")
print(m_product)

# Nesse exemplo, utilizamos a função np.dot() para calcular o produto matricial entre m1 e m2.

# **3.4 Matriz transposta e matriz adjunta**

# A matriz transposta é uma operação que troca as linhas por colunas de uma matriz. A matriz
#  adjunta é uma operação relacionada à matriz transposta, frequentemente usada em matrizes complexas.


# Matriz
m = np.array([[1, 2, 3], [4, 5, 6]])
print(m)

# Matriz transposta
transpose = np.transpose(m)

# Imprimindo resultado
print("Matriz transposta de m:")
print(transpose)


# Explicação: Nesse exemplo, utilizamos a função np.transpose() para calcular a matriz transposta de m.

# **Determinante de uma matriz e sua importância**

# O determinante de uma matriz é uma medida numérica que possui várias aplicações, como testar a 
# inversibilidade da matriz e calcular áreas e volumes.

# Matriz
m = np.array([[1, 2], [3, 4]])

# Determinante de uma matriz
det = np.linalg.det(m)

# Imprimindo resultado
print("Determinante da matriz m:", det)

# Nesse exemplo, utilizamos a função np.linalg.det() para calcular o determinante da matriz m.

# **3.5 Matriz inversa e sua aplicação na resolução de sistemas de equações lineares**

# A matriz inversa é uma operação que nos permite encontrar uma matriz que, quando multiplicada 
# pela matriz original, resulta na matriz identidade. Ela é usada na resolução de sistemas 
# de equações lineares.

# Matriz
m = np.array([[2, 3], [4, 1]])

# Matriz inversa
inverse = np.linalg.inv(m)

# Imprimindo resultado
print("Matriz inversa de m:")
print(inverse)

# Resolução de um sistema de equações lineares
b = np.array([8, 9])
x = np.linalg.solve(m, b)

# Resolução de um sistema de equações lineares por matriz inversa
x1 = inverse.dot(b)

# Imprimindo resultado
print("Solução do sistema de equações lineares:")
print(x)
print(x1)

#Nesse exemplo, utilizamos a função np.linalg.inv() para calcular a matriz 
# inversa de m. Também utilizamos a função np.linalg.solve() para resolver 
# um sistema de equações lineares representado pela matriz m e o vetor b.

