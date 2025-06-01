import pandas as pd

#Lendo o arquivo do Excel de Janeiro e transformando em um DF
vendasJaneiro_DataFrame = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_Jan.xlsx")

#Lendo o arquivo do Excel de Fevereiro e transformando em um DF
vendasFevereiro_DataFrame = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_Fev.xlsx")

#Lendo o arquivo do Excel de Marco e transformando em um DF
vendasMarco_DataFrame = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_Mar.xlsx")

#append - Unindo os dois DataFrame
#append / concat
vendasGeralComGrupos = pd.concat([vendasJaneiro_DataFrame, vendasFevereiro_DataFrame, vendasMarco_DataFrame], keys=["Janeiro", "Fevereiro", "Março"])
# Ordenando pelo valor da coluna "Vendedor" (ordem crescente true) e decrescente false

vendasOrdenado = vendasGeralComGrupos.sort_values(by="Vendedor", ascending=True)
pd.set_option('display.max_rows', 100)  # ou um valor maior que 84 mostra todas as linhas
print(vendasOrdenado)
print('*'*50)
print('*'*50)
print('*'*50)
# Ordenando pelo valor da coluna "Total Vendas" (ordem decrescente)
vendasOrdenado = vendasGeralComGrupos.sort_values(by="Total Vendas", ascending=False)

print(vendasOrdenado)
print('*'*50)
print('*'*50)
print('*'*50)
#Separando o mês de Fevereiro
extraindoFevereiro = vendasGeralComGrupos.loc["Fevereiro"]

#Imprimindo os dados
print(extraindoFevereiro)