import pandas as opcoesPandas
import numpy as opcoesNumpy

'''opcoesPandas é o apelido para o módulo pandas.
date_range cria uma sequência de datas.
"20221231" é a data inicial (31 de dezembro de 2022).
periods=12 indica que serão gerados 12 períodos.
freq="M" define a frequência como "final de cada mês".
Ou seja, ele gera uma lista com as datas do último dia de cada mês, começando em dezembro de 2022, totalizando 12 meses (de dezembro/2022 até novembro/2023). O resultado é um objeto DatetimeIndex com essas datas.'''

#periods = quantos dias
#20221201 = Ano / Mês / Dia
dataFrame_Meses = opcoesPandas.date_range("20221231", periods=12, freq="M")

print(dataFrame_Meses)