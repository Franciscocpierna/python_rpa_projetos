#Importando Imagem do computador para o Excel

import xlsxwriter as opcoesDoXlsxWriter
import os

nomeCaminhoArquivo = 'C:\\python_projetos\\python_rpa_projetos\\python_excel\\ArquivoImagem.xlsx'
workbook = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetPadrao = workbook.add_worksheet("Dados")

#Adicionando dados na Sheet
sheetPadrao.write("B3", "Imagem logo Udemy")

sheetPadrao.insert_image('B5', 'C:\\python_projetos\\python_rpa_projetos\\python_excel\\img.jpg')



#Fechando o arquivo
workbook.close()


#Abrindo o arquivo
os.startfile(nomeCaminhoArquivo)