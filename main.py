import os
import smtplib

from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

from dotenv import load_dotenv

CAMINHO_ARQUIVO = Path(__file__).parent / 'message.html'

load_dotenv()

remetente = os.getenv('EMAIL', '')
destinatario = os.getenv('EMAIL_DESTINATARIO', '')
password = os.getenv('EMAIL_PASSWORD', '')

#Configurações SMTP
smtp_server = os.getenv('SERVER_SMPT', '')
smtp_port = os.getenv('PORT_SMPT')
smtp_user = os.getenv('EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

with open(CAMINHO_ARQUIVO, 'r', encoding="utf-8") as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Samuel')

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Creater -- Company'

#Criando o texto 
corpo_email = MIMEText(texto_email, 'html', 'utf-8')

#Anexando a mensagem
mime_multipart.attach(corpo_email)


# Envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com  sucesso!')
