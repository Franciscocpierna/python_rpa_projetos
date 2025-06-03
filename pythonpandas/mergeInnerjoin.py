import pandas as pd

#Abre o arquivo de Vendas Loja 1 como DataFrame
loja1_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_INNER_JOIN_Loja1.xlsx")

#Abre o arquivo de Vendas Loja 1 como DataFrame
loja2_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_INNER_JOIN_Loja2.xlsx")

#Imprimindo os dados
print(loja1_DF)

#Imprimindo os dados
print(loja2_DF)
print('*'*50)
print('*'*50)
print('*'*50)   
# Realiza um merge (junção) entre os DataFrames loja1_DF e loja2_DF
'''
O how="inner" no merge faz a junção apenas dos dados que existem nas duas tabelas, ou seja, só mostra os vendedores que estão presentes nas duas lojas.
'''
#on = Qual coluna
#how = Como
#inner = Faz o merge entre as tabelas
#Procura e exibe os vendedores que estão em ambas as lojas
vendedoresAmbasLojas_DF = pd.merge(loja1_DF, loja2_DF, on=["Vendedor"], how="inner")
# Exibe todas as colunas e linhas do DataFrame no print
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

#Imprimindo os dados
print(vendedoresAmbasLojas_DF)
#Exibindo os vendedores que estão em ambas as lojas
print('*'*50)
print('*'*50)               
print('*'*50)
#on = Qual coluna
#how = Como
#inner = Faz o merge entre as tabelas
#suffixes = Mudar o nome da coluna 
vendedoresAmbasLojasResumo_DF = pd.merge(loja1_DF, loja2_DF[["Vendedor", "Total Vendas"]], on=["Vendedor"], how="inner", suffixes=(" Loja 1", " Loja 2"))

#Imprimindo os dados
print(vendedoresAmbasLojasResumo_DF)