# ============================================================
# Ejercicio 13: Cafetería - Descuento por consumo
# ============================================================

productos = {
    "cafe": 4000,
    "capuchino": 7000,
    "pastel": 6000
}

total_dia = 0

print("=" * 45)
print("        CAFETERÍA AROMA Y SABOR ☕")
print("=" * 45)
print("Productos disponibles:")
for p, v in productos.items():
    print(f"  - {p}: ${v:,}")
print("\nEscriba 'salir' para terminar el turno.\n")

cliente_num = 0
while True:
    print("-" * 45)
    entrada = input("Producto (o 'salir'): ").strip().lower()
    if entrada == "salir":
        break

    if entrada not in productos:
        print("  ⚠ Producto no válido.")
        continue

    cantidad = 0
    while cantidad <= 0:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                print("  ⚠ Debe ser mayor a 0.")
        except ValueError:
            print("  ⚠ Ingrese un número válido.")

    cliente_num += 1
    subtotal = productos[entrada] * cantidad

    if subtotal > 20000:
        descuento = subtotal * 0.10
        total_cliente = subtotal - descuento
        print(f"  Subtotal        : ${subtotal:,}")
        print(f"  Descuento 10%   : -${descuento:,.0f}")
        print(f"  ✔ Total cliente #{cliente_num}: ${total_cliente:,.0f}")
    else:
        total_cliente = subtotal
        print(f"  ✔ Total cliente #{cliente_num}: ${total_cliente:,}")

    total_dia += total_cliente

print("\n" + "=" * 45)
print("         CIERRE DEL DÍA")
print("=" * 45)
print(f"  Clientes atendidos: {cliente_num}")
print(f"  Total acumulado   : ${total_dia:,.0f}")
print("=" * 45)
