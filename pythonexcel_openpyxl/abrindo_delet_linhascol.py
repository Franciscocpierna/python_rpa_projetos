from openpyxl import load_workbook
import os

#caminho_nome_arquivo = "C:\\Users\\Aluno\\Desktop\\Curso RPA\\openpyxl\\DeletarLinhaColuna.xlsx"
caminho_nome_arquivo ='C:\\python_projetos\\python_rpa_projetos\\pythonexcel_openpyxl\\DeletarLinhaColuna.xlsx'

planilha_aberta = load_workbook(filename=caminho_nome_arquivo)

#Seleciona a sheet de Professor
sheet_selecionada = planilha_aberta['Professor']

#Deleta as linhas
sheet_selecionada.delete_rows(3)
sheet_selecionada.delete_rows(3)
sheet_selecionada.delete_rows(5)

#Deleta a coluna B ou seja coluna 2
sheet_selecionada.delete_cols(2)

#Salva a planilha com as alterações
planilha_aberta.save(filename=caminho_nome_arquivo)

#Abre a planilha
os.startfile(caminho_nome_arquivo)