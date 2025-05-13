from openpyxl import load_workbook
import os

import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

nome_arquivo = "C:\\Users\\Aluno\\Desktop\\Curso RPA\\Separar Arquivo Enviar Email\\ListaEmail.xlsx"
planilha_aberta = load_workbook(filename=nome_arquivo)

sheet_selecionada = planilha_aberta['Dados']

for linha in range(2, len(sheet_selecionada['A']) + 1):
    
    nome = sheet_selecionada['A%s' % linha].value
    nomeCompleto = sheet_selecionada['B%s' % linha].value
    email = sheet_selecionada['C%s' % linha].value
    
    emailOutlook = outlook.CreateItem(0)

    
    emailOutlook.To = email
    emailOutlook.Subject = "Lista de vendas " + nomeCompleto
    emailOutlook.HTMLBody = f"""
    <p>Boa noite <b>{nome}</b>.</p>
    <p>Segue o relatório com suas vendas.</p>
    <p>Atenciosamente.</p>
    <p><img src="C:\\Assinatura\\Udemy Assinatura.jpg">.</p>
    """
    
    anexoEmail = "C:\\Users\\Aluno\\Desktop\\Curso RPA\\Separar Arquivo Enviar Email\\" + nomeCompleto + ".xlsx"
    emailOutlook.Attachments.Add(anexoEmail)

    emailOutlook.save() #save = Cria e salva o email, Send() - Enviar o email
