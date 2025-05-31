import pandas as pd

baseVendas_DF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Base_Vendas.xlsx")

#Imprimindo os dados
print(baseVendas_DF)
#Resumo unicos com nunique
resumoValoresUnicos = baseVendas_DF.nunique()

print('*'*50)
#Imprimindo os dados
print(resumoValoresUnicos)
print('*'*50)
#subset = Identifica a coluna que queremos verificar a duplicidade
#keep = Controla como considerar o valor duplicado (primeiro, último e false considera todos)

#Identificando valores duplicados
confereDuplicidades = baseVendas_DF.duplicated(subset="Vendedor", keep="first")

#Imprimindo os dados
print(confereDuplicidades)

#subset = Identifica a coluna que queremos verificar a duplicidade
#keep = Controla como considerar o valor duplicado (primeiro, último e false considera todos)

#Criando uma nova coluna para conferir as duplicidades first primeiro duplicidades last é o último e False todos que tem duplicidade
baseVendas_DF["Confere Duplicidade"] = baseVendas_DF.duplicated(subset="Vendedor", keep="first")
#Criando uma nova coluna para conferir as duplicidades first primeiro duplicidades last é o último e False todos que tem duplicidade 
#baseVendas_DF["Confere Duplicidade"] = baseVendas_DF.duplicated(subset="Vendedor", keep="last")
#Criando uma nova coluna para conferir as duplicidades first primeiro duplicidades last é o último e False todos que tem duplicidade
#baseVendas_DF["Confere Duplicidade"] = baseVendas_DF.duplicated(subset="Vendedor", keep=False)

print('*'*50)
print('*'*50)
print('*'*50)
#Imprimindo os dados
print(baseVendas_DF)
print('*'*50)
print('*'*50)
print('*'*50)
print('*'*50)
removerDuplicidades = baseVendas_DF.drop_duplicates(subset="Vendedor", keep="first")
print(removerDuplicidades)