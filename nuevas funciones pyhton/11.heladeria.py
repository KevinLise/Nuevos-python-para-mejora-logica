# ============================================================
# Ejercicio 11: Heladería - Factura de varios clientes
# ============================================================

productos = {
    "cono": 3000,
    "vaso": 4000,
    "banana split": 9000
}

total_vendido = 0
clientes_atendidos = 0
conteo_productos = {"cono": 0, "vaso": 0, "banana split": 0}

print("=" * 45)
print("        HELADERÍA EL SABOR FRÍO 🍦")
print("=" * 45)
print("Productos disponibles:")
for p, v in productos.items():
    print(f"  - {p}: ${v:,}")
print()

while True:
    print("-" * 45)
    opcion = input("¿Atender nuevo cliente? (s/n): ").strip().lower()
    if opcion != "s":
        break

    clientes_atendidos += 1
    print(f"\n--- Cliente #{clientes_atendidos} ---")

    producto = ""
    while producto not in productos:
        producto = input("Producto (cono / vaso / banana split): ").strip().lower()
        if producto not in productos:
            print("  ⚠ Producto no válido. Intente de nuevo.")

    cantidad = 0
    while cantidad <= 0:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                print("  ⚠ La cantidad debe ser mayor a 0.")
        except ValueError:
            print("  ⚠ Ingrese un número válido.")

    subtotal = productos[producto] * cantidad
    conteo_productos[producto] += cantidad
    total_vendido += subtotal

    print(f"  ✔ Total cliente #{clientes_atendidos}: ${subtotal:,}")

# Producto más pedido
mas_pedido = max(conteo_productos, key=conteo_productos.get)

print("\n" + "=" * 45)
print("         RESUMEN DEL DÍA")
print("=" * 45)
print(f"  Clientes atendidos : {clientes_atendidos}")
print(f"  Total vendido      : ${total_vendido:,}")
print(f"  Producto más pedido: {mas_pedido} ({conteo_productos[mas_pedido]} unidades)")
print("=" * 45)
