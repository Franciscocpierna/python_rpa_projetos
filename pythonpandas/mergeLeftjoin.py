import pandas as pd

#Abre o arquivo de Vendas Loja 1 como DataFrame
vendas_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_LEFT_JOIN.xlsx")

#Abre o arquivo de Vendas Loja 1 como DataFrame
vendedores_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendedores_LEFT_JOIN.xlsx")

#Imprimindo os dados
print(vendas_DF)

#Imprimindo os dados
print(vendedores_DF)

print('*' * 50)
print('*' * 50)
print('*' * 50)
'''
pd.merge: Função do pandas usada para unir (juntar) dois DataFrames.
vendas_DF: DataFrame da esquerda (base principal, que será mantida).
vendedores_DF: DataFrame da direita (será unido ao da esquerda).
on=["Id Vendedor"]: Especifica a(s) coluna(s) usada(s) como chave(s) para unir os DataFrames. Neste caso, a coluna "Id Vendedor" deve existir em ambos os DataFrames.
how="left": Define o tipo de junção. O "left" faz um LEFT JOIN, ou seja, mantém todas as linhas do DataFrame da esquerda (vendas_DF) e adiciona as informações do DataFrame da direita (vendedores_DF) quando houver correspondência na chave. Se não houver correspondência, os valores das colunas do DataFrame da direita ficam como NaN.
Resumo:
Essa linha faz uma junção entre as vendas e os vendedores, mantendo todas as vendas e trazendo os dados do vendedor correspondente. Se uma venda não tiver vendedor correspondente, as informações do vendedor ficam vazias (NaN).
'''
#on = Coluna
#how = como
#left = Esquerda
#merge = une os arquivos
verificandoVendas_DF = pd.merge(vendas_DF, vendedores_DF, on=["Id Vendedor"], how="left")

#Imprimindo os dados
print(verificandoVendas_DF)
print('*' * 50)
print('*' * 50) 
print('*' * 50)
verificandoVendas_DF = pd.merge(vendas_DF, vendedores_DF, on=["Id Vendedor"], how="left", suffixes=(" Vendas", " Checagem"))

#Imprimindo os dados
print(verificandoVendas_DF)