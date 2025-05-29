import pandas as opcoesPandas
import numpy as opcoesNumpy


''' opcoesPandas é um apelido para o módulo pandas, importado na linha 1.
date_range é uma função do pandas que cria uma sequência de datas.
"20221201" é a data inicial, no formato AAAAMMDD (1º de dezembro de 2022).
periods=31 indica que serão geradas 31 datas consecutivas, começando em 01/12/2022.
O resultado é um objeto DatetimeIndex contendo 31 datas, de 01/12/2022 a 31/12/2022, com intervalo diário. Isso é útil para criar séries temporais ou DataFrames com datas como índice.'''

#periods = quantos dias
#20221201 = Ano / Mês / Dia
dataFrame_Datas = opcoesPandas.date_range("20221201", periods=31)

print(dataFrame_Datas)