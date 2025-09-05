
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inventario inicial
inventario = {
    "Auriculares": 10,
    "Teclado": 5,
    "Mouse": 8,
    "Monitor": 3
}

class Pedido(BaseModel):
    producto: str
    cantidad: int

@app.post("/verificar")
def verificar_stock(pedido: Pedido):
    if pedido.producto not in inventario:
        return {"ok": False, "mensaje": f"Producto {pedido.producto} no existe ❌"}
    elif inventario[pedido.producto] < pedido.cantidad:
        return {"ok": False, "mensaje": f"No hay suficiente stock de {pedido.producto} ❌"}
    else:
        inventario[pedido.producto] -= pedido.cantidad
        return {"ok": True, "mensaje": f"{pedido.cantidad} unidad(es) de {pedido.producto} descontadas 📊"}
    
    
