import pandas as pd

#Abre o arquivo de Vendas como DataFrame
vendasDF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_Merge.xlsx")

#Abre o arquivo de Vendedores como DataFrame
vendedoresDF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendedores_Merge.xlsx")

#Abre o arquivo de Produtos como DataFrame
produtosDF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Produtos_Merge.xlsx")

#merge - Uniu através de um denominador em comum
vendasDF = vendasDF.merge(produtosDF)

#Imprimindo os dados
print(vendasDF)

print('*'*50)
print('*'*50)   
print('*'*50)
#merge - Uniu através de um denominador em comum
vendasDF = vendasDF.merge(vendedoresDF)

#Imprimindo os dados
print(vendasDF)