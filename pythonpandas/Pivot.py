import pandas as pd

#Pivot - Está função não suporta agregação de valores repetitos

baseLanchonete_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_Lanchonete_Pivot.xlsx")

print("\n Imprimindo dados \n")
print(baseLanchonete_DF)
print("\n")

'''
Explicação dos parâmetros:

index="Data Venda": Cada linha da nova tabela será uma data de venda.
columns="Cliente": Cada coluna será um cliente diferente.
values="Preço com Desconto": O valor preenchido na tabela será o preço com desconto correspondente àquela data e cliente.
Resumo:
Você está reorganizando os dados para ver, em cada data de venda (linhas), quanto cada cliente (colunas) pagou pelo produto com desconto. Se houver valores duplicados para a mesma combinação de data e cliente, o método pivot lançará um erro. Para agregação de valores repetidos, use pivot_table em vez de pivot.
'''
#index = linhas
#columns = As colunas
pivotExemplo1 = baseLanchonete_DF.pivot(index="Data Venda", columns="Cliente", values="Preço com Desconto")

print("\n Imprimindo clientes / Preço com Desconto \n")
print(pivotExemplo1)
print("\n")

#--------------------------------------------
'''
Essa linha cria uma tabela dinâmica (pivot table) a partir do DataFrame baseLanchonete_DF usando o método pivot do pandas.

index="Cliente": Cada linha da nova tabela será um cliente diferente.
columns="Data Venda": Cada coluna representará uma data de venda diferente.
values="Preço com Desconto": Os valores da tabela serão os preços com desconto correspondentes a cada cliente em cada data de venda.
O resultado é uma tabela onde você pode ver, para cada cliente (linhas), o preço com desconto pago em cada data de venda (colunas). Se não houver venda para um cliente em determinada data, o valor será NaN.
'''
#index = linhas
#columns = As colunas
pivotExemplo2 = baseLanchonete_DF.pivot(index="Cliente", columns="Data Venda", values="Preço com Desconto")

print("\n Imprimindo clientes / Preço com Desconto \n")
print(pivotExemplo2)
print("\n")