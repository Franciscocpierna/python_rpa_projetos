## Noções de Matemática - Cálculo - Parte 5
### 5. Aplicações de Derivadas

# A derivada tem várias aplicações importantes em diversas áreas da ciência, matemática e engenharia. Algumas das principais aplicações incluem:

# - Determinação de Taxas de Variação e Velocidades Instantâneas: A derivada é usada para calcular taxas de variação de uma quantidade em relação a outra, como velocidades instantâneas em física e taxas de crescimento em economia.
# - Encontrar Pontos Críticos e Extremos: Os pontos críticos são pontos onde a derivada é igual a zero ou não existe, e podem corresponder a mínimos locais, máximos locais ou pontos de inflexão em uma função.
# - Análise de Concavidade e Pontos de Inflexão: A segunda derivada (derivada da derivada) é usada para analisar a concavidade de uma função e identificar pontos de inflexão.
# - Resolução de Problemas de Otimização: A derivada é usada para encontrar valores ótimos em problemas de maximização e minimização.
# **5.1. Taxa de Variação Instantânea e Velocidades Instantâneas**

# Vamos considerar a seguinte função que descreve o movimento de um objeto em uma trajetória retilínea:

# `s(t) = 5t^2 - 2t + 10`

# Vamos calcular a derivada dessa função em relação ao tempo (t) e analisar suas aplicações.

import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Definindo a var iável t
t = sp.symbols('t')

# Definindo a função s(
s_t = 5 * t**2 - 2 * t + 10

# Calculando a derivada da função em relação ao tempo (
derivada_s_t = sp.diff(s_t, t)

# Exibindo a derivada
print("Derivada de s(t) em relação a t:")
print( derivada_s_t)

# Plotando o gráfico da função s(t) e sua derivada
t_values = np.linspace(2, 3, 100)
s_values = [s_t.subs(t, value) for value in t_values]
derivada_values = [derivada_s_t.subs(t, value) for value in t_values]
plt.plot(t_values, s_values, label='s(t) = 5t^2 2t + 10')
plt.plot(t_values, derivada_values, label="s'(t) = 10t 2", linestyle='dashed')
plt.xlabel('t')
plt.ylabel('s(t), s\'(t)')
plt.title('Gráfico de s(t) e sua Derivada')
plt.legend()
plt.grid(True)
plt.show()

# Neste exemplo, calculamos a derivada da função s(t) = 5t^2 - 2t + 10 em relação ao tempo (t) usando a biblioteca sympy. Em seguida, plotamos o gráfico da função original e sua derivada.

# Observe que a derivada s'(t) = 10t - 2 representa a taxa de variação instantânea da posição do objeto em relação ao tempo. A partir do gráfico, podemos analisar a inclinação da função em diferentes pontos e entender o comportamento do movimento do objeto.

# **5.2 Encontrar Pontos Críticos e Extremos (Ex: Máximos e Mínimos Locais)**

# Uma aplicação comum das derivadas é a identificação de máximos e mínimos locais de uma função. Para encontrar esses pontos, podemos procurar os pontos críticos da função, onde a derivada se iguala a zero ou não existe.

# - Máximo local: ocorre quando a derivada muda de positiva para negativa.
# - Mínimo local: ocorre quando a derivada muda de negativa para positiva.


from sympy import Symbol, diff, solve, sin
# Definindo uma variável simbólica 
x = Symbol('x') 

# Exemplo 1: Encontrando máximos e mínimos locais 
f = x**3 - 6*x**2 + 9*x + 2 
derivada = diff(f, x) 
pontos_criticos = solve(derivada, x) 
print("Derivada:", derivada) 
print("Pontos críticos:", pontos_criticos)

#Graficamente, poderiamos ver observar esses pontos ao longo do comportamento dessa função.

import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, diff, solve

# Definindo uma variável simbólica
x = Symbol('x')

# Definindo a função
def f(x):
    return x**3 - 6*x**2 + 9*x + 2

# Calculando a derivada
derivada = diff(f(x), x)

# Encontrando os pontos críticos
pontos_criticos = solve(derivada, x)

# Gerando os valores de x para o gráfico
x_vals = np.linspace(-1, 7, 400)
# Calculando os valores de y correspondentes
y_vals = f(x_vals)

# Plotando o gráfico da função
plt.plot(x_vals, y_vals, label='f(x) = x^3 - 6x^2 + 9x + 2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da função')
plt.grid(True)

# Marcando os pontos críticos no gráfico
for ponto in pontos_criticos:
    plt.plot(ponto, f(ponto), 'ro')  # 'ro' indica um ponto vermelho
    plt.text(ponto, f(ponto), f'({ponto.evalf():3.1f}, {f(ponto).evalf():3.1f})', fontsize=10, verticalalignment='bottom')

plt.legend()
plt.show()

