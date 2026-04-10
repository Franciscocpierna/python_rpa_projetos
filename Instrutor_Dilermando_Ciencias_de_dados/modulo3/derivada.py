# **4.1. Definição de Derivada**

# A derivada é um conceito fundamental do cálculo e representa a taxa de variação instantânea de uma função em relação à sua variável independente. 

# Em outras palavras, a derivada mede a inclinação da função em um ponto específico. 

# A derivada de uma função f(x) em relação a x é denotada por *f'(x)* ou *df/dx*.

# A derivada de uma função f(x) no ponto x é definida como o limite do quociente incremental quando a variável independente (x) se aproxima de zero:

# #### f'(x) = lim_(h → 0) [f(x + h) - f(x)] / h

# Essa expressão representa a taxa de variação instantânea de f(x) em relação a x quando x se aproxima de um valor específico.

# **Interpretação Geométrica**

# Geometricamente, a derivada de uma função em um ponto representa a inclinação da reta tangente à curva da função nesse ponto. Ela indica como a função está mudando em torno desse ponto.

# Aqui está um exemplo:

import numpy as np
import matplotlib.pyplot as plt

# Tempo (em horas)
tempo = np.linspace(0, 10, 100)

# Função que modela a variação da velocidade do veículo ao longo do tempo
def velocidade(tempo):
    return np.maximum(2*tempo - 0.5*tempo**2, 0)  # utilizando np.maximum para garantir que a velocidade não seja negativa

# Calculando a variação da velocidade ao longo do tempo
velocidades = velocidade(tempo)

# Calculando a função de posição (distância percorrida) através da integração da função de velocidade
# Usando o método do trapézio para integração
posicao = np.zeros_like(tempo)
for i in range(1, len(tempo)):
    posicao[i] = posicao[i-1] + 0.5 * (velocidades[i-1] + velocidades[i]) * (tempo[i] - tempo[i-1])

# Plotando o gráfico da função de posição (quilômetros pelo tempo)
plt.figure(figsize=(10, 6))
plt.plot(tempo, posicao, label='Posição')
plt.xlabel('Tempo (horas)')
plt.ylabel('Posição (quilômetros)')
plt.title('Variação da Posição de um Veículo ao Longo do Tempo')
plt.grid(True)
plt.legend()

# Mostrando o gráfico
plt.show()

# Plotando o gráfico da variação da velocidade ao longo do tempo
plt.figure(figsize=(10, 6))
plt.plot(tempo, velocidades, label='Variação da Velocidade')
plt.xlabel('Tempo (horas)')
plt.ylabel('Velocidade (unidades de velocidade)')
plt.title('Variação da Velocidade de um Veículo ao Longo do Tempo')
plt.grid(True)
plt.legend()

# Mostrando o gráfico
plt.show()

#Vamos mostrar graficamente, em um ponto específico (2 horas) qual seria a derivada e a reta tangente a esse ponto.


# Tempo (em horas)
tempo = np.linspace(0, 10, 100)

# Função que modela a variação da velocidade do veículo ao longo do tempo
def velocidade(tempo):
    return np.maximum(2*tempo - 0.5*tempo**2, 0)  # utilizando np.maximum para garantir que a velocidade não seja negativa

# Calculando a variação da velocidade ao longo do tempo
velocidades = velocidade(tempo)

# Calculando a função de posição (distância percorrida) através da integração da função de velocidade
# Usando o método do trapézio para integração
posicao = np.zeros_like(tempo)
for i in range(1, len(tempo)):
    posicao[i] = posicao[i-1] + 0.5 * (velocidades[i-1] + velocidades[i]) * (tempo[i] - tempo[i-1])

# Calculando a derivada da função de posição no ponto específico (t=2 horas)
indice_ponto_especifico = np.argmin(np.abs(tempo - 2))  # Encontrando o índice mais próximo ao tempo especificado
derivada_ponto_especifico = (posicao[indice_ponto_especifico + 1] - posicao[indice_ponto_especifico]) / (tempo[indice_ponto_especifico + 1] - tempo[indice_ponto_especifico])

# Calculando a reta tangente no ponto específico
tempo_tangente = np.linspace(1, 3, 10)  # definindo um intervalo próximo ao ponto específico (2 horas)
posicao_tangente = derivada_ponto_especifico * (tempo_tangente - 2) + posicao[indice_ponto_especifico]  # equação da reta tangente

# Plotando o gráfico da função de posição (quilômetros pelo tempo)
plt.figure(figsize=(10, 6))
plt.plot(tempo, posicao, label='Posição')
plt.xlabel('Tempo (horas)')
plt.ylabel('Posição (quilômetros)')
plt.title('Variação da Posição de um Veículo ao Longo do Tempo')
plt.grid(True)
plt.legend()

# Mostrando o ponto onde a derivada foi calculada
plt.scatter(tempo[indice_ponto_especifico], posicao[indice_ponto_especifico], color='red', label='Ponto Específico')

# Plotando a reta tangente
plt.plot(tempo_tangente, posicao_tangente, '--', color='green', label='Reta Tangente')

# Mostrando o gráfico
plt.show()

print("Derivada no ponto específico (t=2 horas):", derivada_ponto_especifico)

#Também podemos ver algo mais complexo e verificar o comportamento geral da derivada (que agora também passa a ser uma curva)

from sympy import Symbol, diff, exp

# Definindo uma variável simbólica
x = Symbol('x')

# Calculando a derivada
derivada = diff(exp(x**2), x)

print("Derivada:", derivada)


# Neste exemplo, estamos calculando a derivada da função exponencial exp(x^2) em relação a x. A biblioteca SymPy é usada para realizar esse cálculo.

# Uma vez calculado, podemos ver o comportamento dessa relação entre essa função exponencial e x com o seguinte script:

# import numpy as np
# import matplotlib.pyplot as plt
# from sympy import Symbol, diff, exp

# Definindo uma variável simbólica
x = Symbol('x')

# Calculando a derivada da função
derivada = diff(exp(x**2), x)

print("Derivada:", derivada)

# Convertendo a derivada em uma função lambda para avaliação numérica
derivada_func = lambda x_val: derivada.subs(x, x_val)

# Intervalo de valores de x para o gráfico
x_vals = np.linspace(-2, 2, 400)
y_exp = np.exp(x_vals**2)
y_deriv = np.vectorize(derivada_func)(x_vals)

# Configurando o layout do gráfico
plt.figure(figsize=(10, 6))
plt.title("Função Exponencial e sua Derivada")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Plotando a função exponencial e sua derivada
plt.plot(x_vals, y_exp, label="Função Exponencial: $e^{x^2}$")
plt.plot(x_vals, y_deriv, label="Derivada da Função Exponencial")
plt.legend()

# Mostrando o gráfico
plt.show()


# Lembre-se de que a função sympy.diff retorna a derivada simbólica da função, que é representada como uma expressão simbólica. A conversão para uma função numérica é realizada usando lambda e subs para avaliar a derivada em pontos específicos.

# Observando o gráfico, temos:  A função exponencial exp(x ** 2) cresce muito rapidamente à medida que x aumenta. Isso ocorre porque o valor de x ** 2 cresce mais rápido do que x, e quando você aplica a função exponencial, os valores se tornam muito grandes muito rapidamente. Portanto, a curva da função exponencial no gráfico será uma curva ascendente acentuada.

# A derivada da função exponencial exp(x ** 2) em relação a x é calculada e representada no gráfico como a linha que representa a derivada. A derivada dessa função é uma expressão bastante complexa, mas ela também cresce rapidamente à medida que x aumenta. Portanto, a curva da derivada será uma curva ascendente, assim como a função exponencial original.

# O ponto em que a derivada atinge o valor zero (ponto onde a curva da derivada cruza o eixo x) é um ponto crítico da função exponencial. Isso ocorre porque a derivada nos diz onde a função tem uma taxa de variação zero, ou seja, onde ela muda de concavidade. No caso da função exponencial exp(x ** 2), esse ponto crítico está próximo a x = 0.

# Lembre-se de que a derivada da função exponencial é a própria função exponencial multiplicada pelo valor da variável, ou seja, a derivada de exp(x ** 2) em relação a x é 2 * x * exp(x ** 2). Isso contribui para o crescimento rápido da derivada à medida que x aumenta.

# Em resumo, o gráfico ilustra visualmente como a função exponencial exp(x ** 2) cresce rapidamente à medida que x aumenta e como a sua derivada também cresce rapidamente, com um ponto crítico próximo a x = 0. Isso demonstra o comportamento característico de uma função exponencial e sua derivada.

# **4.2. Regras de Derivação**

# As regras de derivação são ferramentas poderosas para simplificar o cálculo de derivadas de funções mais complexas. Essas regras são amplamente utilizadas na Ciência de Dados para calcular derivadas de forma mais eficiente.

# **Regras Básicas de Derivação**

# Existem algumas regras básicas de derivação que podem ser aplicadas em várias situações. Alguns exemplos incluem:

# Regra da soma e da diferença:
# #### (d/dx) [f(x) ± g(x)] = f'(x) ± g'(x)

# Regra do produto:
# #### (d/dx) [f(x) * g(x)] = f'(x) * g(x) + f(x) * g'(x)

# Regra do quociente:
# #### (d/dx) [f(x) / g(x)] = [f'(x) * g(x) - f(x) * g'(x)] / [g(x)]^2

# Regra da cadeia:
# #### (d/dx) [f(g(x))] = f'(g(x)) * g'(x)

# Aqui está um exemplo de como aplicar as regras de derivação em Python usando a biblioteca SymPy:

from sympy import Symbol, diff, sin, cos

# Definindo uma variável simbólica
x = Symbol('x')

# Aplicando as regras de derivação
f = x**2 - 4*x + 4
derivada = diff(f, x)

print("Derivada:", derivada)

#Vamos visualizar graficamente o comportamento dessa função quadrática e em seguida algumas derivadas... mostrando em cada ponto o comportamento / tendência (reta)
# Definindo a função quadrática
def f(x):
    return x**2 - 4*x + 4

# Definindo a derivada da função quadrática
def derivada_f(x):
    return 2*x - 4

# Intervalo de valores de x para o gráfico
x_vals = np.linspace(-1, 5, 400)
y_vals = f(x_vals)

# Pontos onde a derivada será avaliada
pontos = [1, 2, 3]

# Configurando o layout do gráfico
plt.figure(figsize=(10, 6))
plt.title("Gráfico da Função Quadrática e suas Tangentes")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)

# Plotando a função quadrática
plt.plot(x_vals, y_vals, label="Função Quadrática: $x^2 - 4x + 4$")

# Plotando as tangentes à parábola nos pontos onde a derivada é avaliada
for ponto in pontos:
    x_ponto = ponto
    y_ponto = f(x_ponto)
    m_tangente = derivada_f(x_ponto)
    y_tangente = m_tangente * (x_vals - x_ponto) + y_ponto
    plt.plot(x_vals, y_tangente, '--', label=f"Tangente em x={x_ponto}")

# Adicionando marcadores nos pontos de interseção
pontos_intersecao = [(1, 2), (2, 0), (3, 2)]
for ponto in pontos_intersecao:
    plt.plot(ponto[0], ponto[1], 'ro')  # 'ro' indica um ponto vermelho
    plt.text(ponto[0], ponto[1], f'({ponto[0]}, {ponto[1]})', fontsize=10, verticalalignment='bottom')

plt.legend()
plt.show()

#Um outro exemplo, mais complexo... Apenas para exemplificar.

# Definindo uma variável simbólica
x = Symbol('x')

# Aplicando as regras de derivação
f = sin(x) * cos(x)
derivada = diff(f, x)

print("Derivada:", derivada)

# Neste exemplo, estamos calculando a derivada da função sin(x) * cos(x) em relação a x. A biblioteca SymPy é usada para simplificar a expressão e aplicar as regras de derivação.

# O script a seguir mostra como será o comportamento dessa derivada graficamente:

# Definindo uma variável simbólica
x = Symbol('x')

# Definindo a função
f = sin(x) * cos(x)

# Calculando a derivada
derivada = diff(f, x)

print("Derivada:", derivada)

# Convertendo a derivada em uma função lambda para avaliação numérica
derivada_func = lambda x_val: derivada.subs(x, x_val)

# Intervalo de valores de x para o gráfico
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y_function = np.sin(x_vals) * np.cos(x_vals)
y_derivative = np.vectorize(derivada_func)(x_vals)

# Configurando o layout do gráfico
plt.figure(figsize=(10, 6))
plt.title("Função e sua Derivada")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Plotando a função e sua derivada
plt.plot(x_vals, y_function, label="Função: $sin(x) * cos(x)$")
plt.plot(x_vals, y_derivative, label="Derivada da Função")
plt.legend()

# Mostrando o gráfico
plt.show()

# A função sin(x) * cos(x) possui comportamento oscilatório, e sua derivada mostrará a taxa de variação dessas oscilações ao longo do intervalo. 

# A derivada será zero nos pontos onde a função cruza o eixo x (máximos e mínimos locais) e atingirá valores máximos nos pontos médios entre esses extremos.

# O gráfico ilustrará esse comportamento.
# **4.3. Derivadas de Funções Elementares**

# As funções elementares são funções básicas que são amplamente utilizadas na Ciência de Dados. É importante conhecer as derivadas dessas funções para poder calcular derivadas de funções mais complexas.

# **Derivadas de Funções Elementares Comuns**

# Aqui estão algumas das derivadas das funções elementares mais comuns:

# Derivada da função constante:
# #### (d/dx) [c] = 0

# Derivada da função linear:
# #### (d/dx) [ax + b] = a

# Derivada da função exponencial:
# #### (d/dx) [e^x] = e^x

# Derivada da função logarítmica:
# #### (d/dx) [ln(x)] = 1/x

# Derivada da função seno:
# #### (d/dx) [sin(x)] = cos(x)

# Derivada da função cosseno:
# #### (d/dx) [cos(x)] = -sin(x)

# Aqui está um exemplo de como calcular as derivadas de funções elementares em Python usando a biblioteca SymPy:

from sympy import Symbol, diff, exp, log, sin, cos

# Definindo uma variável simbólica
x = Symbol('x')

# Calculando as derivadas de funções elementares
derivada_constante = diff(5, x)
derivada_linear = diff(3*x + 2, x)
derivada_exponencial = diff(exp(x), x)
derivada_logaritmica = diff(log(x), x)
derivada_seno = diff(sin(x), x)
derivada_cosseno = diff(cos(x), x)

print("Derivada da função constante:", derivada_constante)
print("Derivada da função linear:", derivada_linear)
print("Derivada da função exponencial:", derivada_exponencial)
print("Derivada da função logarítmica:", derivada_logaritmica)
print("Derivada da função seno:", derivada_seno)
print("Derivada da função cosseno:", derivada_cosseno)


