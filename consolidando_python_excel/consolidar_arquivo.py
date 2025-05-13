import pandas as opcoesDoPanda
import os

#Caminho onde estão os arquivos
#caminhoArquivos = r"C:\Users\Aluno\Desktop\Curso RPA\Consolindando_python_excel\Excel"
caminhoArquivos = r"C:\python_projetos\python_rpa_projetos\Consolidando_python_excel"

#Variável onde estão todos os arquivos
listaArquivos = os.listdir(caminhoArquivos)

print(listaArquivos)

#Listando todos os arquivos + o caminho
listaCaminhoEArquivoExcel = [caminhoArquivos + '\\' + arquivo for arquivo in listaArquivos if arquivo[-4:] == 'xlsx' ]

print("----- #### -------- ###### ---------")
print("----- #### -------- ###### ---------")
print(listaCaminhoEArquivoExcel)

#Criando um DataFrame para trabalhar com os dados dos arquivos
dadosArquivo = opcoesDoPanda.DataFrame()

#Copiando todos os dados dos arquivos em DadosArquivo
listaDados = []  # Lista para armazenar os DataFrames temporariamente
for arquivo in listaCaminhoEArquivoExcel:
    dados = opcoesDoPanda.read_excel(arquivo)
    #dadosArquivo = dadosArquivo.append(dados) descontinuado append
    # Adicionando o DataFrame à lista
    listaDados.append(dados)
dadosArquivo = opcoesDoPanda.concat(listaDados, ignore_index=True)

#Criando uma nova planilha e passando os dados dos arquivos
dadosArquivo.to_excel(r"C:\python_projetos\python_rpa_projetos\Consolidando_python_excel\Arquivo Consolidado.xlsx")
