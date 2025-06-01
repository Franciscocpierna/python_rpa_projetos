import pandas as pd

baseVendas_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Ordenação.xlsx")

#Imprimindo os dados
print(baseVendas_DF)

#sort_values = Ordena
#by - Coluna
print('*'*50)
print('*'*50)   
print('*'*50)
ordenarVendedor = baseVendas_DF.sort_values(by="Vendedor")

#Imprimindo os dados
print(ordenarVendedor)
print('*'*50)
print('*'*50)   
print('*'*50)
#sort_values = Ordena
#by - Coluna
ordenarProduto = baseVendas_DF.sort_values(by="Produto")

#Imprimindo os dados
print(ordenarProduto)

print('*'*50)
print('*'*50)   
print('*'*50)
#sort_values = Ordena
#by - Coluna
#ordenarDataVenda = baseVendas_DF.sort_values(by="Data Venda")

# Converter a coluna "Data Venda" para datetime, se ainda não for
baseVendas_DF["Data Venda"] = pd.to_datetime(baseVendas_DF["Data Venda"])

# Formatar a coluna "Data Venda" para o formato dd/mm/aaaa
baseVendas_DF["Data Venda"] = baseVendas_DF["Data Venda"].dt.strftime('%d/%m/%Y')

# Agora, ao ordenar, a data estará formatada
ordenarDataVenda = baseVendas_DF.sort_values(by="Data Venda")


#Imprimindo os dados
print(ordenarDataVenda)

print('*'*50)
print('*'*50)
print('*'*50)

#sort_values = Ordena
#by - Coluna
ordenarDuasColunas = baseVendas_DF.sort_values(by=["Vendedor", "Produto"])

#Imprimindo os dados
print(ordenarDuasColunas)
print('*'*50)
print('*'*50)   
print('*'*50)
#ascending - Do maior para o menor
ordenarZaA = baseVendas_DF.sort_values(by="Vendedor", ascending=False)

#Imprimindo os dados
print(ordenarZaA)

print('*'*50)
print('*'*50)               
print('*'*50)

#ascending - Do maior para o menor
ordenarZaA_TotalVendas = baseVendas_DF.sort_values(by="Total Vendas", ascending=False)

#Imprimindo os dados
print(ordenarZaA_TotalVendas)
total_geral = ordenarZaA_TotalVendas["Total Vendas"].sum()
print("Total Geral de Vendas:", total_geral)

