import matplotlib.pyplot as plt
import numpy as np

# Função que descreve a concentração de álcool no vinho em relação ao envelhecimento
def Concentracao_de_alcool(envelhecimento):
    return 14 - 0.2 * envelhecimento

# Valores para o envelhecimento do vinho (de 0 a 50 anos)
envelhecimento = np.linspace(0, 50, 100)

# Calculando os valores de concentração de álcool usando a função
concentracao = Concentracao_de_alcool(envelhecimento)

# Plotando o gráfico da concentração de álcool versus envelhecimento
plt.plot(envelhecimento, concentracao)
plt.xlabel('Envelhecimento (anos)')
plt.ylabel('Concentração de Álcool (%)')
plt.title('Concentração de Álcool no Vinho com o Envelhecimento')
plt.grid(True)
plt.show()


def Concentracao_no_sangue(tempo):
    return 0.1 * tempo

# Valores para o tempo após ingestão do vinho (de 0 a 5 horas)
tempo = np.linspace(0, 5, 100)

# Calculando os valores de concentração de álcool no sangue usando a função
concentracao_sangue = Concentracao_no_sangue(tempo)

# Plotando o gráfico da concentração de álcool no sangue versus tempo após ingestão
plt.plot(tempo, concentracao_sangue)
plt.xlabel('Tempo após ingestão (horas)')
plt.ylabel('Concentração de Álcool no Sangue (%)')
plt.title('Concentração de Álcool no Sangue após Ingestão de Vinho')
plt.grid(True)
plt.show()

# Função que descreve o nível de amizade em relação à quantidade de vinho compartilhado
def Nivel_de_amizade(qtd_vinho_compartilhado):
    return 50 + 2 * qtd_vinho_compartilhado

# Valores para a quantidade de vinho compartilhado (de 0 a 10 litros)
qtd_vinho_compartilhado = np.linspace(0, 10, 100)

# Calculando os valores de nível de amizade usando a função
nivel_amizade = Nivel_de_amizade(qtd_vinho_compartilhado)

# Plotando o gráfico do nível de amizade versus quantidade de vinho compartilhado
plt.plot(qtd_vinho_compartilhado, nivel_amizade)
plt.xlabel('Quantidade de Vinho Compartilhado (litros)')
plt.ylabel('Nível de Amizade')
plt.title('Nível de Amizade em Relação à Quantidade de Vinho Compartilhado')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

def funcao_linear(x, m, b):
    return m * x + b

# Valores para a função linear
m = 2
b = 5
x = range(-10, 11)  # Valores de x de -10 a 10

# Calculando os valores de y
y = [funcao_linear(i, m, b) for i in x]

# Plotando o gráfico
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da Função Linear')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

def funcao_quadratica(x, a, b, c):
    return a * x**2 + b * x + c

# Valores para a função quadrática
a = 1
b = -2
c = 1
x = range(-10, 11)  # Valores de x de -10 a 10

# Calculando os valores de y
y = [funcao_quadratica(i, a, b, c) for i in x]

# Plotando o gráfico
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da Função Quadrática')
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt

def funcao_exponencial(x, a):
    return a ** x

# Valores para a função exponencial
a = 2
x = range(-10, 11)  # Valores de x de -10 a 10

# Calculando os valores de y
y = [funcao_exponencial(i, a) for i in x]

# Plotando o gráfico
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da Função Exponencial')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

def funcao_logaritmica(x, a):
    return np.log(x) / np.log(a)

# Valores para a função logarítmica
a = 2
x = np.linspace(0.1, 10, 100)  # Valores de x de 0.1 a 10 (o log não é definido para x=0)

# Calculando os valores de y
y = [funcao_logaritmica(i, a) for i in x]

# Plotando o gráfico
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da Função Logarítmica')
plt.grid(True)
plt.show()




