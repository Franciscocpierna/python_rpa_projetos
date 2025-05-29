import pandas as opcoesPandas
import numpy as opcoesNumpy

'''
Esse comando cria um DataFrame do pandas chamado numerosAleatorios contendo números aleatórios gerados pelo numpy. Veja o que cada parte faz:

opcoesNumpy.random.rand(5,1): Gera uma matriz 5x1 (5 linhas, 1 coluna) de números aleatórios entre 0 e 1.
opcoesPandas.DataFrame(...): Converte essa matriz em um DataFrame do pandas, facilitando a manipulação e análise dos dados.
Ou seja, ao final, numerosAleatorios é uma tabela com 5 linhas e 1 coluna, preenchida com valores aleatórios.
'''

#DataFrame de números aleatórios
numerosAleatorios = opcoesPandas.DataFrame(opcoesNumpy.random.rand(5,1))

print(numerosAleatorios)
