TOTAL_VENTAS = 10
categorias_validas = ("alimento", "juguete", "accesorio")

ventas = {"alimento": 0, "juguete": 0, "accesorio": 0}

print("=" * 45)
print("      TIENDA DE MASCOTAS PATITAS ")
print("=" * 45)
print(f"Registrar {TOTAL_VENTAS} ventas.")
print("Categorías: alimento | juguete | accesorio\n")

for i in range(1, TOTAL_VENTAS + 1):
    print(f"--- Venta {i} de {TOTAL_VENTAS} ---")

    categoria = ""
    while categoria not in categorias_validas:
        categoria = input("Categoría: ").strip().lower()
        if categoria not in categorias_validas:
            print("   Categoría no válida.")

    valor = 0
    while valor <= 0:
        try:
            valor = float(input("Valor de la compra: $"))
            if valor <= 0:
                print("   Debe ser mayor a 0.")
        except ValueError:
            print("   Ingrese un número válido.")

    ventas[categoria] += valor
    print(f"   Registrado en '{categoria}'\n")

categoria_top = max(ventas, key=ventas.get)

print("=" * 45)
print("       RESUMEN DE VENTAS DEL DÍA")
print("=" * 45)
for cat, total in ventas.items():
    print(f"  {cat.capitalize():12}: ${total:,.0f}")
print(f"\n   Mayor ingreso: {categoria_top} (${ventas[categoria_top]:,.0f})")
print("=" * 45)
