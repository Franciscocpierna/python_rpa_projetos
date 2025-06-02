import pandas as pd

dadosFrameDados = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Tratamento_Dados.xlsx")

#ffill - Preenche os valores com o último registro válido no caso foi 502
dadosFrameDados["Total Vendas"] = dadosFrameDados["Total Vendas"].ffill()

#Imprimindo os dados
print(dadosFrameDados)