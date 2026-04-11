## Noções de Matemática - Álgebra Linear - Parte 2
## 2. Vetores

# Os vetores são estruturas matemáticas que representam uma quantidade com magnitude e direção 
# em um espaço específico.

# **2.1 Definição e propriedades de vetores**

# Vamos começar definindo vetores e explorando algumas de suas propriedades.

import numpy as np

# Definindo vetores
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Imprimindo vetores
print("Vetor v1:", v1)
print("Vetor v2:", v2)

# Tamanho dos vetores
size_v1 = len(v1)
size_v2 = len(v2)
print("Tamanho do vetor v1:", size_v1)
print("Tamanho do vetor v2:", size_v2)

# Acessando elementos de um vetor
element_v1 = v1[0]
element_v2 = v2[1]
print("Elemento de índice 0 do vetor v1:", element_v1)
print("Elemento de índice 1 do vetor v2:", element_v2)

# Nesse exemplo, criamos dois vetores v1 e v2. Utilizamos a função len() para obter o tamanho dos vetores e a notação de índice para acessar elementos específicos.

# **2.2 Operações com vetores: adição, subtração e multiplicação por escalar**

# Vamos explorar as operações básicas com vetores: adição, subtração e multiplicação por escalar.

# Vetores
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Operações com vetores
v_sum = v1 + v2
v_diff = v1 - v2
v_scalar_mul = 2 * v1

# Imprimindo resultados
print("Soma de vetores v1 + v2:", v_sum)
print("Subtração de vetores v1 - v2:", v_diff)
print("Multiplicação escalar de v1 por 2:", v_scalar_mul)

# Nesse exemplo, realizamos a adição de v1 e v2, a subtração de v1 por v2 e a multiplicação
#  de v1 por um escalar de 2.

# **2.3 Produto escalar e suas aplicações**

# O produto escalar (também conhecido como produto interno) é uma operação que combina 
# dois vetores, produzindo um número real.


# Vetores
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Produto escalar
dot_product = np.dot(v1, v2)

# Imprimindo resultado
print("Produto escalar entre v1 e v2:", dot_product)


# Nesse exemplo, utilizamos a função np.dot() para calcular o produto escalar entre v1 e v2.

# **2.4 Norma de um vetor e distância euclidiana**

# A norma de um vetor é uma medida que representa o comprimento ou magnitude do vetor.

# Vetor
v = np.array([1, 2, 3])

# Norma de um vetor
norm = np.linalg.norm(v)

# Imprimindo resultado
print("Norma do vetor v:", norm)


# Nesse exemplo, utilizamos a função np.linalg.norm() para calcular a norma do vetor v.

# **2.5 Vetores ortogonais e produto vetorial**

# Dois vetores são considerados ortogonais se o ângulo entre eles for de 90 graus. 
# O produto vetorial é uma operação que produz um novo vetor que é ortogonal aos dois vetores originais.

# Vetores
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])

# Produto vetorial
cross_product = np.cross(v1, v2)

# Imprimindo resultado
print("Produto vetorial entre v1 e v2:", cross_product)


#Nesse exemplo, utilizamos a função np.cross() para calcular o produto vetorial entre v1 e v2.