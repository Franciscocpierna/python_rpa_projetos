#Formatacao Condicional
import xlsxwriter as opcoesDoXlsxWriter
import os

#nomeCaminhoArquivo = 'C:\\Users\\Aluno\\Desktop\\Curso RPA\\xlsxwriter\\FormatacaoCondicional.xlsx'
nomeCaminhoArquivo = 'C:\\python_projetos\\python_rpa_projetos\\python_excel\\FormatacaoCondicional.xlsx'
planilhaExcel = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetDados = planilhaExcel.add_worksheet("Dados")

#Adiciona um formato de preenchimento verde com o texto em branco
formatoMaior = planilhaExcel.add_format({'bg_color': 'green',
                                        'font_color': 'white'})

#Adiciona um formato de preenchimento vermelho com o texto em branco
formatoMenor = planilhaExcel.add_format({'bg_color': 'red',
                                        'font_color': 'white'})

#Coloca alguns dados de amostra para executar a formatação condicional
inserirDados = [
    ["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
    [34, 50, 12, 34],
    [59, 58, 76, 51],
    [43, 80, 34, 12],
    [91, 58, 73, 19],
]


sheetDados.write('A1', "Células com valores >= 50 estão em verde e < 50 estão em vermelho")


for linha, range in enumerate(inserirDados):
    sheetDados.write_row(linha + 2, 1, range) #Linha 3, coluna 2
    
sheetDados.conditional_format('B4:E7', {'type': 'cell',
                                       'criteria': '>=',
                                       'value': 50,
                                       'format': formatoMaior})

sheetDados.conditional_format('B4:E7', {'type': 'cell',
                                       'criteria': '<',
                                       'value': 50,
                                       'format': formatoMenor})

#Fechando o arquivo
planilhaExcel.close()


#Abrindo o arquivo
os.startfile(nomeCaminhoArquivo)