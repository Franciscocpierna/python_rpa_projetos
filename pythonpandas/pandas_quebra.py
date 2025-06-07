import pandas as pd

#Abre o arquivo de Vendas_Jan como DataFrame
baseDados_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_Jan.xlsx")

#Imprimindo os dados
print(baseDados_DF)

print("*" * 50)
print("*" * 50) 
print("*" * 50)
'''
drop_duplicates: É um método do pandas que remove linhas duplicadas do DataFrame.
subset="Vendedor": Indica que a verificação de duplicidade será feita apenas na coluna "Vendedor". Ou seja, se houver mais de uma linha com o mesmo nome de vendedor, será considerada duplicada.
keep="first": Diz para manter a primeira ocorrência de cada vendedor e remover as demais.
'''
#subset - Coluna que queremos remover
#keep - Instrução do qual valor vai permanecer (first / primeiro)
removendoDuplicidades = baseDados_DF.drop_duplicates(subset="Vendedor", keep="first")

#Imprimindo os dados
print(removendoDuplicidades)

print("*" * 50)
print("*" * 50) 
print("*" * 50)

#for - para
#in - onde
for linha in removendoDuplicidades["Vendedor"]:
    
    print(linha)

#Imprimindo os dados
#display(removendoDuplicidades)

print("*" * 50)
print("*" * 50) 
print("*" * 50)
'''
Esse trecho percorre cada vendedor único e, para cada um, filtra e imprime todas as vendas feitas por ele, usando o DataFrame original (que pode ter várias vendas por vendedor).

Exemplo prático
Se você tem os vendedores "Ana", "Bruno" e "Carlos", o código vai:

Pegar "Ana", filtrar todas as vendas dela e imprimir.
Depois "Bruno", filtrar todas as vendas dele e imprimir.
E assim por diante.
'''
#for - para
#in - onde
for linha in removendoDuplicidades["Vendedor"]:
    
    #loc - Localizar
    vendas_Funcionario = baseDados_DF.loc[baseDados_DF["Vendedor"] == linha]
    print(vendas_Funcionario)

#Imprimindo os dados
#display(removendoDuplicidades)
print("*" * 50)
print("*" * 50) 
print("*" * 50)

for linha in removendoDuplicidades["Vendedor"]:
    
    #loc - Localizar
    vendas_Funcionario = baseDados_DF.loc[baseDados_DF["Vendedor"] == linha]
    
    #Salvando o arquivo em formato excel csv
    vendas_Funcionario.to_csv("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\arqporvendedor\\Relatório Vendas " + linha + ".csv")
    
print("Relatório separado com sucesso!")
print("*" * 50)
print("*" * 50)
print("*" * 50)
for linha in removendoDuplicidades["Vendedor"]:
    
    #loc - Localizar
    vendas_Funcionario = baseDados_DF.loc[baseDados_DF["Vendedor"] == linha]
    
    #engine - mecamismo da biblioteca xlsxwriter
    #Salvando o arquivo em formato excel xlsx
    arquivoExcel = pd.ExcelWriter("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\arqporvendedor\\outros\\Relatório Vendas " + linha + ".xlsx", engine="xlsxwriter")
    arquivoExcel.close()
    
    #Transformando os dados no DataFrame
    dataFrame = pd.DataFrame(vendas_Funcionario)
    
    #Preparar o arquivo
    arquivoExcel = pd.ExcelWriter("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\arqporvendedor\\outros\\Relatório Vendas " + linha + ".xlsx", engine="xlsxwriter")
    
    #Convertendo o DataFrame em um arquivo de Excel
    dataFrame.to_excel(arquivoExcel, sheet_name="Dados", index=False)
    
    #Salvo as modificações
    arquivoExcel.close()
    
print("Relatório separado com sucesso!")