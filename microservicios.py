# microservicios.py
import time

# --- Inventario inicial ---
inventario = {
    "Auriculares": 10,
    "Teclado": 5,
    "Mouse": 8,
    "Monitor": 3
}

# --- Microservicios simulados ---
def servicio_pagos(monto):
    print("Servicio de Pagos: procesando pago...")
    time.sleep(1)
    return f"Pago de ${monto} aprobado ✅"

def servicio_inventario(producto, cantidad):
    print("Servicio de Inventario: verificando stock...")
    time.sleep(0.5)
    if producto not in inventario:
        return False, f"Producto '{producto}' no existe ❌"
    elif inventario[producto] < cantidad:
        return False, f"No hay suficiente stock de '{producto}' ❌"
    else:
        inventario[producto] -= cantidad
        return True, f"{cantidad} unidad(es) de '{producto}' descontadas del inventario 📊"

def servicio_envios(ciudad):
    print("Servicio de Envíos: registrando envío...")
    time.sleep(1)
    return f"Paquete registrado para envío a {ciudad} 📦"

# --- Función para mostrar inventario ---
def mostrar_inventario():
    print("\n=== Inventario Actual ===")
    for prod, cant in inventario.items():
        print(f"{prod}: {cant} unidad(es)")
    print("========================\n")

# --- Función para agregar productos ---
def agregar_producto():
    nombre = input("Ingrese el nombre del nuevo producto: ")
    cantidad = int(input("Ingrese la cantidad inicial: "))
    if nombre in inventario:
        inventario[nombre] += cantidad
        print(f"Se agregaron {cantidad} unidad(es) a '{nombre}'.")
    else:
        inventario[nombre] = cantidad
        print(f"Producto '{nombre}' agregado al inventario con {cantidad} unidad(es).")

# --- Orquestador principal ---
def sistema_compra():
    print("=== Sistema de Microservicios ===")
    
    while True:
        mostrar_inventario()
        print("Opciones:")
        print("1 - Comprar producto")
        print("2 - Agregar producto al inventario")
        print("3 - Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "3":
            print("Saliendo del sistema...")
            break
        elif opcion == "2":
            agregar_producto()
        elif opcion == "1":
            producto = input("Ingrese el producto a comprar: ")
            cantidad = int(input("Ingrese la cantidad: "))

            # Verificar inventario primero
            hay_stock, mensaje_inventario = servicio_inventario(producto, cantidad)
            if not hay_stock:
                print(mensaje_inventario + "\n")
                continue  # No procesar pago ni envío si no hay stock

            monto = float(input("Ingrese el monto a pagar: "))
            ciudad = input("Ingrese la ciudad de destino: ")

            resultado_pago = servicio_pagos(monto)
            resultado_envios = servicio_envios(ciudad)

            print("\n--- Resultados ---")
            print(resultado_pago)
            print(mensaje_inventario)
            print(resultado_envios)
            print("\nCompra finalizada con éxito 🎉\n")
        else:
            print("Opción inválida, intente de nuevo.\n")

# --- Ejecutar ---
if __name__ == "__main__":
    sistema_compra()