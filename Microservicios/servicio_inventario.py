
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # creamos la app de fastAPI

# Inventario inicial
inventario = {
    "Auriculares": 10,
    "Teclado": 5,
    "Mouse": 8,
    "Monitor": 3
}

#Modelo de pedido que espera producto y cantidad
class Pedido(BaseModel):
    producto: str
    cantidad: int

@app.post("/verificar") # Ruta para verificar stock
def verificar_stock(pedido: Pedido):
    # Si el producto no existe
    if pedido.producto not in inventario:
        return {"ok": False, "mensaje": f"Producto {pedido.producto} no existe ❌"}
    
    # Si no hay suficiente stock
    elif inventario[pedido.producto] < pedido.cantidad:
        return {"ok": False, "mensaje": f"No hay suficiente stock de {pedido.producto} ❌"}
    else:
        # Si hay stock, descontamos la cantidad
        inventario[pedido.producto] -= pedido.cantidad
        return {"ok": True, "mensaje": f"{pedido.cantidad} unidad(es) de {pedido.producto} descontadas 📊"}
    
    
