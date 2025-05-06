
from openpyxl import load_workbook
import os

caminho_nome_arquivo = "C:\\python_projetos\\python_rpa_projetos\\pythonexcel_openpyxl\\InserirDados.xlsx"
planilha_aberta = load_workbook(filename=caminho_nome_arquivo)

#Seleciona a sheet de Professor
sheet_selecionada = planilha_aberta['Professor']

#Popula as informações que vão para a planilha
dadosTabela = [
    ['Nome', 'Idade'],
    ['Berenice', 28],
    ['Caio', 32],
    ['Nicole', 34],
    ['Leonardo', 19],
    ['Amanda', 25]
]

#O append pega toda a lista e passa para a sheet
for linhaPlanilha in dadosTabela:
    sheet_selecionada.append(linhaPlanilha)



#Salva a planilha com as alterações
planilha_aberta.save(filename=caminho_nome_arquivo)

#Abre a planilha
os.startfile(caminho_nome_arquivo)