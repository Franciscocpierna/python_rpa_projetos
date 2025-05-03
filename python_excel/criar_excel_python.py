import xlsxwriter as opcoesDoXlsxWriter
import os

#nomeCaminhoArquivo = 'C:\\Users\\Aluno\\Desktop\\Curso RPA\\xlsxwriter\\PrimeiroExemplo.xlsx'
nomeCaminhoArquivo = 'C:\\python_projetos\\python_rpa_projetos\\python_excel\\PrimeiroExemplo.xlsx'
workbook = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetPadrao = workbook.add_worksheet()

#Adicionando dados na Sheet
sheetPadrao.write("A1", "Nome")
sheetPadrao.write("B1", "Idade")
sheetPadrao.write("A2", "Amanda")
sheetPadrao.write("B2", 21)
sheetPadrao.write("A3", "Allan")
sheetPadrao.write("B3", 28)


#Fechando o arquivo
workbook.close()


#Abrindo o arquivo
os.startfile(nomeCaminhoArquivo)
