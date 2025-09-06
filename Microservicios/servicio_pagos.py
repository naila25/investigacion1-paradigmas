
import time
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de pago que espera el monto a pagar
class Pago(BaseModel):
    monto: float


@app.post("/procesar") # Ruta para procesar pagos

def procesar_pago(pago: Pago):
    time.sleep(1)  # Simula procesamiento
    return {"ok": True, "mensaje": f"Pago de ${pago.monto} aprobado ✅"}