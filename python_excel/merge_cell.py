import xlsxwriter as opcoesDoXlsxWriter
import os

#nomeCaminhoArquivo = 'C:\\Users\\Aluno\\Desktop\\Curso RPA\\xlsxwriter\\MergeCells.xlsx'
nomeCaminhoArquivo = 'C:\\python_projetos\\python_rpa_projetos\\python_excel\\MergeCells.xlsx'
workbook = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetPadrao = workbook.add_worksheet()

add_merge_celulas = workbook.add_format({
        'bold': True,
        'border' : 6,
        'align' : 'center',
        'valign' : 'vcenter',
        'size' : 30,
        'fg_color' : 'blue',
        'font_color' : 'white',
})

sheetPadrao.merge_range('B3:I5', 'Aula de Merge Células', add_merge_celulas)


#Fechando o arquivo
workbook.close()


#Abrindo o arquivo
os.startfile(nomeCaminhoArquivo)