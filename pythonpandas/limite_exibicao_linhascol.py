import pandas as pd

#Configurando o caminho do arquivo
vendas_DataFrame = pd.read_excel ("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_Jan.xlsx") #Lê o arquivo Excel e cria um DataFrame

print(vendas_DataFrame)# Exibe o DataFrame completo 
print()
print()
print()
#Exibe informações sobre quantidade de linhas que tem o DF
print(vendas_DataFrame.index)
print()
print()
print()
#colums - informações sobre quantidade de colunas que tem o DF
print(vendas_DataFrame.columns)
print()
print()
print()
#head - exibe as 5 primeiras linhas do DF
print(vendas_DataFrame.head())
print()
print()
print()
#head - exibe quantas linhas forem determinado
print(vendas_DataFrame.head(10)) # Exibe as 10 primeiras linhas do DataFrame
print()
print()
print()
print()
#tail - exibe as últimas linhas
print(vendas_DataFrame.tail(5))# Exibe as últimas 5 linhas do DataFrame e quantas linhas forem determinado
print()
print()
print()
print()
#Limitando colunas, imprimindo apenas uma coluna e head() limitando a quantidade de linhas em 5
print(vendas_DataFrame["Vendedor"].head())
print()
print()
print()
print()

#Limitando colunas, imprimindo apenas duas colunas e head() limitando a quantidade de linhas em 5
print(vendas_DataFrame[["Vendedor", "Total Vendas"]].head())
print()
print()
print()
print()
#loc - localiza e limita a quantidade de linha
print(vendas_DataFrame.loc[1:5])
print()
print()
print()
print()
