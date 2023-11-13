from fastapi import FastAPI, HTTPException
from emails.classes.c_mail import EmailSchema
from emails.funcs.send_mail import enviar_correo
import threading
import os

app = FastAPI()




@app.get('/')
def index():
    return 'q onda mondonga'


@app.post('/email_sender')
def email_sender(Email: EmailSchema):
    
    print(Email)
    enviar_correo(Email.destinatarios, Email.sujeto, Email.mensaje)
    

    return {"mensaje": "Correo enviado exitosamente"}
