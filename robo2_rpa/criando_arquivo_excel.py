#versão excel 2003
import os
import xlwt

# Caminho do arquivo Excel
nomeCaminhoArquivo = "C:\\python_projetos\\python_rpa_projetos\\robo2_rpa\\Dolar+e+Euro+Google.xls"

# Criando o arquivo Excel
planilhaCriada = xlwt.Workbook()
sheet1 = planilhaCriada.add_sheet("Dados")

# Escrevendo nas células
sheet1.write(0, 0, "Nome")  # Linha 0, Coluna 0
sheet1.write(0, 1, "Idade")  # Linha 0, Coluna 1
sheet1.write(1, 0, "Amanda")  # Linha 1, Coluna 0
sheet1.write(1, 1, 28)  # Linha 1, Coluna 1
sheet1.write(2, 0, "Roberto")  # Linha 2, Coluna 0
sheet1.write(2, 1, 25)  # Linha 2, Coluna 1

# Salvando o arquivo Excel
planilhaCriada.save(nomeCaminhoArquivo)


# Abrindo o arquivo
os.startfile(nomeCaminhoArquivo)

'''
import xlsxwriter # versão mais nova do excel 
import os

nomeCaminhoArquivo = "A:\\Python RPA\\Extraindo Valor do Dolar e Euro e Salvando no Excel\\Dolar e Euro Google.xlsx"
planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo)
sheet1 = planilhaCriada.add_worksheet()

#Escrevendo nas células
sheet1.write("A1", "Nome")
sheet1.write("B1", "Idade")
sheet1.write("A2", "Amanda")
sheet1.write("B2", 28)
sheet1.write("A3", "Roberto")
sheet1.write("B3", 25)

#Fechando o arquivo do Excel que está em segundo plano
planilhaCriada.close()

#Abro o arquivo
os.startfile(nomeCaminhoArquivo)


'''