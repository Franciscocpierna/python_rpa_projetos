
import pandas as pd

#Abre o arquivo de Vendas_Lanchonete_Pivot como DataFrame
baseLanchonete_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_Lanchonete_Pivot_Table.xlsx")

#Imprimindo os dados
print(baseLanchonete_DF)

print("*" * 50)
print("*" * 50)
print("*" * 50)


# Pivot Table - Permite agregação de valores repetidos

'''
pivot_table: Método do pandas que cria uma tabela dinâmica (pivot table), semelhante ao recurso do Excel.
Parâmetros usados:

index="Data Venda"
Define que cada linha da tabela dinâmica será uma data de venda diferente.

columns="Cliente"
Cada coluna da tabela dinâmica será um cliente diferente.

values="Preço com Desconto"
Os valores que vão preencher a tabela serão retirados da coluna "Preço com Desconto".

aggfunc="sum"
Se houver mais de um valor para a mesma combinação de data e cliente, eles serão somados.

Resultado:
Você terá uma tabela onde:

As linhas representam as datas de venda.
As colunas representam os clientes.
As células mostram o total de "Preço com Desconto" vendido para cada cliente em cada data.
Se não houver vendas para um cliente em uma data, a célula ficará vazia (Na
'''

#index - Linhas
#columns - Colunas
#values - Coluna a ser somana
#aggfunc - Função para colocarmos para somar os itens na pivot_table sem ela, por padrão os valores vem como média
pivotExemplo1 = baseLanchonete_DF.pivot_table(index="Data Venda", columns="Cliente", values="Preço com Desconto", aggfunc="sum")

#Imprimindo os dados
print(pivotExemplo1)

print("*" * 50)
print("*" * 50) 
print("*" * 50)


#index - Linhas
#columns - Colunas
#values - Coluna a ser somana
#aggfunc - Função para colocarmos para somar os itens na pivot_table sem ela, por padrão os valores vem como média
pivotExemplo1 = baseLanchonete_DF.pivot_table(index="Data Venda", columns="Cliente", values="Preço com Desconto")

#Imprimindo os dados
print(pivotExemplo1)
print("*" * 50)
print("*" * 50) 
print("*" * 50)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#index - Linhas
#columns - Colunas
#values - Coluna a ser somana
#aggfunc - Função para colocarmos para somar os itens na pivot_table sem ela, por padrão os valores vem como média
pivotExemplo2 = baseLanchonete_DF.pivot_table(index="Data Venda", columns="Cliente", values=["Preço Total","Preço com Desconto"], aggfunc="sum")

#Imprimindo os dados
print(pivotExemplo2)

print("*" * 50)
print("*" * 50)
print("*" * 50)

#index - Linhas
#columns - Colunas
#values - Coluna a ser somana
#aggfunc - Função para colocarmos para somar os itens na pivot_table sem ela, por padrão os valores vem como média
pivotExemplo2 = baseLanchonete_DF.pivot_table(index="Data Venda", columns=["Cliente", "Produto"], values="Preço com Desconto", aggfunc="sum")

#Imprimindo os dados
print(pivotExemplo2)
print("*" * 50)
print("*" * 50) 
print("*" * 50)
#index - Linhas
#columns - Colunas
#values - Coluna a ser somana
#aggfunc - Função para colocarmos para somar os itens na pivot_table sem ela, por padrão os valores vem como média
pivotExemplo2 = baseLanchonete_DF.pivot_table(index="Data Venda", columns=["Cliente", "Produto"],  values=["Preço Total","Preço com Desconto"], aggfunc="sum")
pivotExemplo2["Preço Total"] = pivotExemplo2["Preço Total"].fillna(0)
pivotExemplo2["Preço com Desconto"] = pivotExemplo2["Preço com Desconto"].fillna(0)

#Imprimindo os dados
print(pivotExemplo2)