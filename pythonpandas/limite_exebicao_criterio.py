import pandas as pd

#Configurando o caminho do arquivo
vendas_DataFrame = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_Jan.xlsx")

#loc - localiza e limita um critério
vendas_Leonardo_Almeida_DF = vendas_DataFrame.loc[vendas_DataFrame["Vendedor"] == "Leonardo Almeida"]


print(vendas_Leonardo_Almeida_DF)

#loc - localiza e limita um critério
vendas_Leonardo_Almeida_DF = vendas_DataFrame.loc[vendas_DataFrame["Vendedor"] == "Leonardo Almeida", ["Vendedor", "Total Vendas"]]
print()
print()
print()

print(vendas_Leonardo_Almeida_DF)
print()
print()
print()
#shape - Mostra quantas linhas e quantas coluna tem no DF
print(vendas_DataFrame.shape)

