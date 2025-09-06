
import requests

def sistema_compra():
    print("=== Sistema de Compras con Microservicios ===")
    
    # Pedimos al usuario el producto y la cantidad
    producto = input("Ingrese el producto a comprar: ")
    cantidad = int(input("Ingrese la cantidad: "))

     # Llamamos al microservicio de inventario
    r1 = requests.post("http://127.0.0.1:8000/verificar", json={"producto": producto, "cantidad": cantidad})
    resp1 = r1.json()
    print(resp1["mensaje"])
    if not resp1["ok"]:
        return

    # Llamamos al microservicio de pagos
    monto = float(input("Ingrese el monto a pagar: "))
    r2 = requests.post("http://127.0.0.1:8001/procesar", json={"monto": monto})
    resp2 = r2.json()
    print(resp2["mensaje"])

   # Llamamos al microservicio de envíos
    ciudad = input("Ingrese la ciudad de destino: ")
    r3 = requests.post("http://127.0.0.1:8002/registrar", json={"ciudad": ciudad})
    resp3 = r3.json()
    print(resp3["mensaje"])

    print("\nCompra finalizada con éxito 🎉")

if __name__ == "__main__":
    sistema_compra()
