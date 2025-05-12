#Criando um email simples 
import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

emailOutlook = outlook.CreateItem(0)

emailOutlook.To = "ana@gmail.com"
emailOutlook.Subject = "Meu primeiro email usando Python e Outlook"
emailOutlook.HTMLBody = """
<p>Boa noite Ana.</p>
<p>Esse é apenas um email de teste.</p>
<p>Atenciosamente.</p>
"""

emailOutlook.save() #save = Cria e salva o email, Send() - Enviar o email