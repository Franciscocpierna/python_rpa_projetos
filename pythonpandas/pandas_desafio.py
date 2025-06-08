import pandas as pd


#https://docs.google.com/spreadsheets/d/1uxYa8NKhoPQVAO_LNqNWxyn30qn5S_qD/edit?usp=sharing&ouid=103286032416998039927&rtpof=true&sd=true

planilha_id = '1uxYa8NKhoPQVAO_LNqNWxyn30qn5S_qD'

dados_DF = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{planilha_id}/export?format=csv")

print(dados_DF)


"""
Desafio

1 - Após carregar os dados, deixe somente as colunas de Vendedor e Total de Vendas
2 - Com o groupby, use a coluna de vendedor para criar um resumo do vendedor e a soma total das vendas
3 - Salve o dataFrame como um arquivo de Excel

Parece fácil, mas não é! Boa sorte!

"""

#1 - Após carregar os dados, deixe somente as colunas de Vendedor e Total de Vendas

#drop - Deletar
deletarDuasColunas = dados_DF.drop(columns=["Produto", "Data Venda"])


#2 - Com o groupby, use a coluna de vendedor para criar um resumo do vendedor e a soma total das vendas

#Substituindo tudo que é virgula por ponto na coluna Total Vendas
deletarDuasColunas["Total Vendas"] = deletarDuasColunas["Total Vendas"].str.replace(',','.') 

#Convertendo a coluna Total Vendas de texto para float
deletarDuasColunas["Total Vendas"] = deletarDuasColunas["Total Vendas"].astype(float)

groupbyVendedor = deletarDuasColunas.groupby(["Vendedor"]).sum()


print(groupbyVendedor)

#3 - Salve o dataFrame como um arquivo de Excel

#Salvando o arquivo como excel csv
groupbyVendedor.to_csv("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\desafio\\Resposta Desafio.csv")

#engine - mecamismo da biblioteca xlsxwriter
#Salvando o arquivo em formato excel xlsx
arquivoExcel = pd.ExcelWriter("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\desafio\\Resposta Desafio.xlsx", engine="xlsxwriter")
arquivoExcel.close()
    
#Transformando os dados no DataFrame
dataFrame = pd.DataFrame(groupbyVendedor)
    
#Preparar o arquivo
arquivoExcel = pd.ExcelWriter("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\desafio\\Resposta Desafio.xlsx", engine="xlsxwriter")
    
#Convertendo o DataFrame em um arquivo de Excel
dataFrame.to_excel(arquivoExcel, sheet_name="Dados", index=True)

#Salvo as modificações
arquivoExcel.close()