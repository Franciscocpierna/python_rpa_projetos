import pandas as pd

vendasJaneiro_DataFrame = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_Jan.xlsx")

#Imprimindo os dados
print(vendasJaneiro_DataFrame)
print('*'*50)
print('*'*50)
print('*'*50)
#Lendo o arquivo do Excel de Fevereiro e transformando em um DF
vendasFevereiro_DataFrame = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_Fev.xlsx")

#Imprimindo os dados
print(vendasFevereiro_DataFrame)

print('*'*50)
print('*'*50)   
print('*'*50)

#append - Unindo os dois DataFrame
#append / concat
#vendasJaneiro_DataFrame = vendasJaneiro_DataFrame.append(vendasFevereiro_DataFrame) append está obsoleto
# ...existing code...
vendasJaneiro_DataFrame = pd.concat([vendasJaneiro_DataFrame, vendasFevereiro_DataFrame], ignore_index=True)
# ...existing code...    

#Imprimindo os dados
print(vendasJaneiro_DataFrame)
print('*'*50)
print('*'*50)       
print('*'*50)
#Remunindo / Pegando apenas 3 colunas do DF
resumindo_DataFrame = vendasJaneiro_DataFrame[["Vendedor", "Data Venda", "Total Vendas"]] 

#Imprimindo os dados
print(resumindo_DataFrame)
