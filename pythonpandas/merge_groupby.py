import pandas as pd

#Abre o arquivo de Groupby como DataFrame
vendas_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Groupby.xlsx")

#Imprimindo os dados
print(vendas_DF)

print('*'*50)
print('*'*50)
print('*'*50)
#mean = Média
#groupby = Agrupando
#mediaVendedor = vendas_DF.groupby(["Vendedor"]).mean()
#mediaVendedor = vendas_DF.groupby("Vendedor")["Total Vendas"].mean()
mediaVendedor = vendas_DF.groupby("Vendedor")[["Preço", "Qtd", "Total Vendas"]].mean()
#Preço	Qtd	
#Imprimindo os dados
print(mediaVendedor)

print('*'*50)
print('*'*50)   
print('*'*50)

#sum = Soma
#groupby = Agrupando
#somaVendedor = vendas_DF.groupby(["Vendedor"]).sum()
somaVendedor = vendas_DF.groupby("Vendedor")[["Preço", "Qtd", "Total Vendas"]].sum()
#somaVendedor = vendas_DF.groupby(["Vendedor"])["Total Vendas"].sum()


#Imprimindo os dados
print(somaVendedor)

print('*'*50)
print('*'*50)   
print('*'*50)

#sum = Soma
#groupby = Agrupando
#dropna=False = Não deleto os valores em branco
#deixandoValoresEmBranco = vendas_DF.groupby(["Vendedor"], dropna=False) ["Total Vendas"].sum()
deixandoValoresEmBranco = vendas_DF.groupby(["Vendedor"], dropna=False)[["Preço", "Qtd", "Total Vendas"]].sum()
#Imprimindo os dados
print(deixandoValoresEmBranco)
print('*'*50)
print('*'*50)           
print('*'*50)
#sum = Soma
#groupby = Agrupando
#dropna=False = Não deleto os valores em branco
#agrupaDuasColunas = vendas_DF.groupby(["Vendedor", "Produto"]).sum()
agrupaDuasColunas = vendas_DF.groupby(["Vendedor", "Produto"])[["Preço", "Qtd", "Total Vendas"]].sum()
#
#Imprimindo os dados
print(agrupaDuasColunas)

print('*'*50)
print('*'*50)   
print('*'*50)

#sum = Soma
#groupby = Agrupando
#dropna=False = Não deleto os valores em branco
agrupaFrutasVendedor = vendas_DF.groupby(["Produto", "Vendedor"])[["Preço", "Qtd", "Total Vendas"]].sum()

#Imprimindo os dados
print(agrupaFrutasVendedor)
print('*'*50)
print('*'*50)   
print('*'*50)
#sum = Soma
#groupby = Agrupando
#dropna=False = Não deleto os valores em branco
agrupaDataVendedor = vendas_DF.groupby(["Data Venda", "Vendedor"])[["Preço", "Qtd", "Total Vendas"]].sum()

#Imprimindo os dados
print(agrupaDataVendedor)