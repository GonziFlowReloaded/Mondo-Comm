from flask import Flask, request
from dotenv import load_dotenv
import smtplib
import os
load_dotenv()
app = Flask(__name__)


def adapter(res):
    destinatarios = res['destinatarios']
    sujeto = res['sujeto']
    mensaje = res['mensaje']
    enviar_correo(destinatarios, sujeto, mensaje)
    return {"message": "Mensaje enviado"}

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


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/email_sender", methods=['POST'])
def send_message():
    adapter(request.json)
    return {"status": 200,
            "message": "Mails enviados"}


if __name__ == '__main__':
    app.run(debug=True)