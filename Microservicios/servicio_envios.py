
from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI() # Creamos la app de FastAPI

# Modelo de envío que espera la ciudad de destino
class Envio(BaseModel):
    ciudad: str

@app.post("/registrar")# Ruta para registrar envíos 

def registrar_envio(envio: Envio):
    time.sleep(1)  # Simula registro del envio 
    return {"ok": True, "mensaje": f"Paquete registrado para envío a {envio.ciudad} 📦"}
