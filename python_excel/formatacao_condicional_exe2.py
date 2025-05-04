#Formatacao Condicional com Icones
import xlsxwriter as opcoesDoXlsxWriter
import os

#nomeCaminhoArquivo = 'C:\\Users\\Aluno\\Desktop\\Curso RPA\\xlsxwriter\\FormatacaoCondicionalIcones.xlsx'
nomeCaminhoArquivo = 'C:\\python_projetos\\python_rpa_projetos\\python_excel\\FormatacaoCondicionalIcones.xlsx'
planilhaExcel = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetDados = planilhaExcel.add_worksheet("Dados")


#Coloca alguns dados de amostra para executar a formatação condicional
inserirDados = [
    ["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
    [34, 50, 12, 34],
    [59, 58, 76, 51],
    [43, 80, 34, 12],
    [91, 58, 73, 19],
    [18, 30, 45, 12],
]


sheetDados.write('A1', "Exemplos de formatação condicional com conjunto de ícones")


for linha, range in enumerate(inserirDados):
    sheetDados.write_row(linha + 2, 1, range) #Linha 3, coluna 2
    
sheetDados.conditional_format('B4:E4', {'type': 'icon_set',
                                       'icon_style': '3_traffic_lights'})

sheetDados.conditional_format('B5:E5', {'type': 'icon_set',
                                       'icon_style': '3_traffic_lights',
                                       'reverse_icons': True})

sheetDados.conditional_format('B6:E6', {'type': 'icon_set',
                                       'icon_style': '3_arrows'})

sheetDados.conditional_format('B7:E7', {'type': 'icon_set',
                                       'icon_style': '4_arrows'})

sheetDados.conditional_format('B8:E8', {'type': 'icon_set',
                                       'icon_style': '5_ratings'})



#Fechando o arquivo
planilhaExcel.close()


#Abrindo o arquivo
os.startfile(nomeCaminhoArquivo)