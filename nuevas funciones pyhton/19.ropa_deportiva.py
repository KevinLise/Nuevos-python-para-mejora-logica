TOTAL_PRODUCTOS = 10
agotados = stock_bajo = stock_normal = 0

print("=" * 45)
print("    TIENDA DEPORTIVA SPRINT ")
print("=" * 45)
print(f"Registrar {TOTAL_PRODUCTOS} productos.\n")

for i in range(1, TOTAL_PRODUCTOS + 1):
    print(f"--- Producto {i} de {TOTAL_PRODUCTOS} ---")

    nombre = input("Nombre del producto: ").strip()

    cantidad = -1
    while cantidad < 0:
        try:
            cantidad = int(input("Cantidad disponible: "))
            if cantidad < 0:
                print("   No puede ser negativo.")
        except ValueError:
            print("   Ingrese un número válido.")

    if cantidad == 0:
        estado = "agotado"
        agotados += 1
    elif cantidad <= 5:
        estado = "stock bajo"
        stock_bajo += 1
    else:
        estado = "stock normal"
        stock_normal += 1

    print(f"   {nombre}: {cantidad} unidades → {estado}\n")

print("=" * 45)
print("       RESUMEN DE INVENTARIO")
print("=" * 45)
print(f"  Agotados     (0)     : {agotados}")
print(f"  Stock bajo   (1-5)   : {stock_bajo}")
print(f"  Stock normal (6+)    : {stock_normal}")
print("=" * 45)
