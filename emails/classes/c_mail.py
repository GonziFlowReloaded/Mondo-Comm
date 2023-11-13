from pydantic import BaseModel

class EmailSchema(BaseModel):
    destinatarios: list
    sujeto: str
    mensaje: str