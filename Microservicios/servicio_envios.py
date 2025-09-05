
from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI()

class Envio(BaseModel):
    ciudad: str

@app.post("/registrar")
def registrar_envio(envio: Envio):
    time.sleep(1)  # Simula registro
    return {"ok": True, "mensaje": f"Paquete registrado para envío a {envio.ciudad} 📦"}
