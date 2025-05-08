import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor SMTP
smtp_server = "smtp.seuprovedor.com"  # Exemplo: smtp.gmail.com
smtp_port = 587  # Porta comum para SMTP com TLS
email_usuario = "seuemail@exemplo.com"
email_senha = "suasenha"

# Configuração do e-mail
destinatario = "destinatario@exemplo.com"
assunto = "Assunto do E-mail"
corpo = "Este é o corpo do e-mail."

# Criar a mensagem
mensagem = MIMEMultipart()
mensagem["From"] = email_usuario
mensagem["To"] = destinatario
mensagem["Subject"] = assunto
mensagem.attach(MIMEText(corpo, "plain"))

# Enviar o e-mail
try:
    with smtplib.SMTP(smtp_server, smtp_port) as servidor:
        servidor.starttls()  # Inicia a conexão segura
        servidor.login(email_usuario, email_senha)
        servidor.sendmail(email_usuario, destinatario, mensagem.as_string())
        print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")