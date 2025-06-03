import pandas as pd

#Abre o arquivo de Vendas Loja 1 como DataFrame
loja1_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_INNER_JOIN_Loja1.xlsx")
#Abre o arquivo de Vendas Loja 1 como DataFrame
loja2_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_INNER_JOIN_Loja2.xlsx")

#on = Qual coluna
#how = Como
#inner = Faz o merge entre as tabelas
#suffixes = Mudar o nome da coluna 
vendedoresAmbasLojasResumo_DF = pd.merge(loja1_DF, loja2_DF[["Vendedor", "Total Vendas"]], on=["Vendedor"], how="inner", suffixes=(" Loja 1", " Loja 2"))

resumo = vendedoresAmbasLojasResumo_DF[["Vendedor", "Total Vendas Loja 1", "Total Vendas Loja 2"]]

#Imprimindo os dados
print(resumo)