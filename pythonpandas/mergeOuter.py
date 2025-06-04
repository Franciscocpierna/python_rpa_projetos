import pandas as pd

#Abre o arquivo de Vendas Loja 1 como DataFrame
vendasLoja1_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Outer_Vendas_Loja1.xlsx")

#Abre o arquivo de Vendas Loja 1 como DataFrame
vendasLoja2_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Outer_Vendas_Loja2.xlsx")

#Imprimindo os dados
print(vendasLoja1_DF)

#Imprimindo os dados
print(vendasLoja2_DF)

print('*'*50)
print('*'*50)
print('*'*50)

#on = Coluna
#how = como
#merge = une os arquivos
verificandoVendas_DF = pd.merge(vendasLoja1_DF, vendasLoja2_DF, on=["Id Vendedor"], how="outer", suffixes=(" Loja 1", " Loja 2"))

#Imprimindo os dados
print(verificandoVendas_DF)
print('*'*50)
print('*'*50)

#on = Coluna
#how = como
#merge = une os arquivos
verificandoVendas_DF = pd.merge(vendasLoja1_DF, vendasLoja2_DF, on=["Id Vendedor"], how="outer", suffixes=(" Loja 1", " Loja 2"))

#dropna = Deleta as linhas que contém pelo menos um valor em branco
tratamentoDados_DF = verificandoVendas_DF.dropna()

#Imprimindo os dados
print(tratamentoDados_DF)

print('*'*50)
print('*'*50)       
print('*'*50)

#on = Coluna
#how = como
#merge = une os arquivos
verificandoVendas_DF = pd.merge(vendasLoja1_DF, vendasLoja2_DF, on=["Id Vendedor"], how="outer", suffixes=(" Loja 1", " Loja 2"))

#dropna = Deleta as linhas que contém pelo menos um valor em branco
tratamentoDados_DF = verificandoVendas_DF.dropna()

del tratamentoDados_DF["Vendedor Loja 2"]

#Imprimindo os dados
print(tratamentoDados_DF)