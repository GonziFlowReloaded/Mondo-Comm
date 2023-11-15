import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

def enviar_correo(destinatarios, sujeto, mensaje):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        email = os.getenv('MONDO_MAIL')
        password = os.getenv('MONDO_MAIL_PASS')
        print(email, password)
        smtp.login(email, password)

        for destinatario in destinatarios:
            asunto = sujeto
            headers = f'From: {email}\nTo: {destinatario}\nSubject: {asunto}\n'
            msg = f'{headers}\r\n{mensaje}'
            smtp.sendmail(email, destinatario, msg)
