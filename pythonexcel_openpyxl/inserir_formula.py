from openpyxl import load_workbook
import os

caminho_nome_arquivo = "C:\\python_projetos\\python_rpa_projetos\\pythonexcel_openpyxl\\Formulas.xlsx"

planilha_aberta = load_workbook(filename=caminho_nome_arquivo)

#Seleciona a sheet de Professor
sheet_selecionada = planilha_aberta['Professor']

#Preenchendo as formulas de sum e operações
sheet_selecionada['A6'] = "=SUM(A2:A5)"
sheet_selecionada['B6'] = "=SUM(B2:B5)"
sheet_selecionada['D2'] = "=A2+B2"
sheet_selecionada['D3'] = "=A3-B3"
sheet_selecionada['D4'] = "=A4*B4"
sheet_selecionada['D5'] = "=A5/B5"

#Preenchendo as formulas de MID para separar o CPF em partes
sheet_selecionada['B12'] = "=MID(A12,1,3)"
sheet_selecionada['C12'] = "=MID(A12,5,3)"
sheet_selecionada['D12'] = "=MID(A12,9,3)"
sheet_selecionada['E12'] = "=MID(A12,13,2)"


#Salva a planilha com as alterações
planilha_aberta.save(filename=caminho_nome_arquivo)

#Abre a planilha
os.startfile(caminho_nome_arquivo)