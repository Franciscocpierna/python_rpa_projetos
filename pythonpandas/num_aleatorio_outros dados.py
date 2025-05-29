import pandas as opcoesPandas
import numpy as opcoesNumpy

'''opcoesNumpy.random.rand(15,10): Gera uma matriz de 15 linhas e 10 colunas com números aleatórios entre 0 e 1.
*100: Multiplica todos esses números por 100, transformando-os em valores entre 0 e 100.
opcoesPandas.DataFrame(...): Converte essa matriz em um DataFrame do pandas, que é uma tabela com 15 linhas e 10 colunas, facilitando a manipulação e análise dos dados.
Resumindo: você cria uma tabela (DataFrame) com 15 linhas e 10 colunas, preenchida com números aleatórios entre 0 e 100.'''


#DataFrame de números aleatórios
numeros = opcoesPandas.DataFrame(opcoesNumpy.random.rand(15,10)*100)

print(numeros)