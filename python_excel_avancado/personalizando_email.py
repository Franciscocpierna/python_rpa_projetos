#Criando um email simples
import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

emailOutlook = outlook.CreateItem(0)

email = "ana@gmail.com"
variavelNome = "Ana"

emailOutlook.To = email
emailOutlook.Subject = "Meu primeiro email usando Python e Outlook"
emailOutlook.HTMLBody = f"""
<p>Boa noite <b>{variavelNome}</b>.</p>
<p><font color="red"><b><u>Esse é apenas um email de teste.</b></u></font></p>
<p><a href="https://www.google.com/">Clique aqui para acessar o nosso site.</a></p>
<p>Atenciosamente.</p>
<p><img src="C:\\Assinatura\\Udemy Assinatura.jpg">.</p>
"""

emailOutlook.save() #save = Cria e salva o email, Send() - Enviar o email