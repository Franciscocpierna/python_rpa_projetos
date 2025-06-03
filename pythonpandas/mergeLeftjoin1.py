import pandas as pd

#Abre o arquivo de Vendas Loja 1 como DataFrame
vendas_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_LEFT_JOIN.xlsx")

#Abre o arquivo de Vendas Loja 1 como DataFrame
vendedores_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendedores_LEFT_JOIN.xlsx")

#on = Coluna
#how = como
#left = Esquerda
#merge = une os arquivos
verificandoVendas_DF = pd.merge(vendas_DF, vendedores_DF, on=["Id Vendedor"], how="left", suffixes=(" Vendas", " Checagem"))

#dropna = Deleta todas as linhas que tem pelo menos 1 valor vazio
limpandoLinhasComNAN = verificandoVendas_DF.dropna()

#Imprimindo os dados
print(limpandoLinhasComNAN)