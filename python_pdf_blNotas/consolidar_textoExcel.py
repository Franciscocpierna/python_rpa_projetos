import pandas as opcoesPandas
import os

#Caminho onde estão os arquivos
caminhoArquivos = "C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\consolidar"

#Variável onde estão todos os arquivos
listaArquivos = os.listdir(caminhoArquivos)

print(listaArquivos)

listaCaminhoEArquivoBlocoNotas = [caminhoArquivos + '\\' + arquivo for arquivo in listaArquivos if arquivo[-3:] == 'txt']

print(listaCaminhoEArquivoBlocoNotas)

#Criando os DataFrame para trabalhar com os Dados
dadosArquivo = opcoesPandas.DataFrame()

#Copiando todos os dados dos arquivos em dadosArquivo
for arquivo in listaCaminhoEArquivoBlocoNotas:
    
    #Pego as informações de cada bloco de notas e armazeno como um DF em Dados
    dados = opcoesPandas.read_csv(arquivo)
    
    #Junto / Consolido / Concateno os dados de todos os DF em dadosArquivo
    dadosArquivo = opcoesPandas.concat([dadosArquivo, dados])
    
#Criando uma nova planilha e passando os dados dos arquivos
#dadosArquivo.to_excel("A:\\Python RPA\\Arquivo Texto e PDF\\Arquivo Consolidado.xlsx")
dadosArquivo.to_csv('C:\\python_projetos\\python_rpa_projetos\\python_pdf_blNotas\\consolidar\\Arquivo Consolidado.csv', encoding='utf-8-sig')