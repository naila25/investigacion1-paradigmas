
import time
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Pago(BaseModel):
    monto: float


@app.post("/procesar")
def procesar_pago(pago: Pago):
    time.sleep(1)  # Simula procesamiento
    return {"ok": True, "mensaje": f"Pago de ${pago.monto} aprobado ✅"}