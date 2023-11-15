from emails.funcs.send_mail import enviar_correo

def adapter(res):
    destinatarios = res['destinatarios']
    sujeto = res['sujeto']
    mensaje = res['mensaje']
    enviar_correo(destinatarios, sujeto, mensaje)
    return {"message": "Mensaje enviado"}