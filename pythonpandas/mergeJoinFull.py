import pandas as pd

#Abre o arquivo de Vendas Loja 1 como DataFrame
loja1_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendedores_Join_Full_Loja1.xlsx")

#Abre o arquivo de Vendas Loja 1 como DataFrame
loja2_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendedores_Join_Full_Loja2.xlsx")

#Imprimindo os dados
print(loja1_DF)

#Imprimindo os dados
print(loja2_DF)
print('*' * 50)
print('*' * 50)
print('*' * 50)

#concat = Uni os DataFrame
#Join Full - Juntar Tudo
vendasLoja_1_e_2_DF = pd.concat([loja1_DF, loja2_DF])

#Imprimindo os dados
print(vendasLoja_1_e_2_DF)
print('*' * 50)
print('*' * 50)             
print('*' * 50)

semClientesDuplicados = vendasLoja_1_e_2_DF.drop_duplicates(subset="Id Vendedor")

#Imprimindo os dados
print(semClientesDuplicados)