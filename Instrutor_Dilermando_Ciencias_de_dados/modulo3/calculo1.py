

# Neste exemplo, ao calcular o limite **lim_(x → 2) f(x)**, obtemos o valor 4. Isso significa que a função tende a 4 quando x se aproxima de 2.

# Este é apenas um exemplo simples de como calcular limites usando Python e a biblioteca sympy, que nos permite trabalhar simbolicamente com expressões matemáticas. 

# Vamos ilustrar graficamente o comportamento de algumas funções quando o valor de x se aproxima de um determinado valor c. Para isso, vamos usar as técnicas de simplificação direta e fatoração para calcular os limites.

import matplotlib.pyplot as plt
import numpy as np

# Funções que queremos analisar
def f1(x):
    return (x**2 - 4) / (x - 2)

def f2(x):
    return np.sin(x) / x

def f3(x):
    return x * np.cos(1/x)

# Valores para x
x = np.linspace(-10, 10, 500)

# Valor de c para os limites
c = 3

# Cálculo dos limites usando as funções definidas
limite_f1 = f1(c)
limite_f2 = f2(c)
limite_f3 = f3(c)

# Plotando os gráficos das funções
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(x, f1(x))
plt.axvline(x=c, color='red', linestyle='--', label=f'Limite: {limite_f1}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da Função (x^2 - 4) / (x - 2)')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(x, f2(x))
plt.axvline(x=c, color='red', linestyle='--', label=f'Limite: {limite_f2}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da Função sin(x) / x')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(x, f3(x))
plt.axvline(x=c, color='red', linestyle='--', label=f'Limite: {limite_f3}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da Função x * cos(1/x)')
plt.legend()

plt.tight_layout()
plt.show()

# Mais um exemplo de cálculo de Limite...

# Aqui está um exemplo de como aplicar as regras de cálculo de limites em Python usando a biblioteca SymPy...

from sympy import Symbol, limit, sin, cos

# Definindo uma variável simbólica
x = Symbol('x')

# Aplicando regras de cálculo de limites
f = sin(x) * cos(x)
limite = limit(f, x, 0)

print("Limite:", limite)

# **3.3. Continuidade de Funções**

# A continuidade de uma função é uma propriedade importante que descreve a existência de limites e a suavidade da função em um determinado intervalo. Na Ciência de Dados, a continuidade é relevante para garantir a validade dos modelos e das análises realizadas.

# **Definição de Função Contínua**

# Uma função é considerada contínua em um ponto se o limite da função existe nesse ponto e é igual ao valor da função naquele ponto. Uma função é considerada contínua em um intervalo se for contínua em cada ponto desse intervalo.

# **Tipos de Descontinuidades**

# Existem diferentes tipos de descontinuidades que podem ocorrer em funções:

# •	**Descontinuidade Removível**: ocorre quando uma função possui uma descontinuidade em um ponto, mas pode ser tornada contínua atribuindo um valor adequado à função nesse ponto.

# •	**Descontinuidade de Salto**: ocorre quando uma função tem uma diferença finita entre os limites do ponto de descontinuidade.

# •	**Descontinuidade Infinita**: ocorre quando uma função tem um limite infinito em um ponto de descontinuidade.

# Aqui está um exemplo de como verificar a continuidade de uma função em Python usando a biblioteca SymPy:
# Definindo uma variável simbólica
from math import pi
from sympy import *
x = Symbol('x')

# Verificando a continuidade da função
f = sin(x)
continuidade_em_0 = f.subs(x, 0)
continuidade_em_pi = f.subs(x, pi)
continuidade_em_inf = f.limit(x, oo)

print("Continuidade em x=0:", continuidade_em_0)
print("Continuidade em x=pi:", continuidade_em_pi)
print("Continuidade em x=∞:", continuidade_em_inf)