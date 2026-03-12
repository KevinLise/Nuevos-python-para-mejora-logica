TOTAL_CLIENTES = 7
servicios_validos = ("corte", "cepillado", "tintura")

total_dia = 0
conteo_servicios = {"corte": 0, "cepillado": 0, "tintura": 0}

print("=" * 45)
print("         PELUQUERÍA GLAMOUR ")
print("=" * 45)
print(f"Atendiendo {TOTAL_CLIENTES} clientes hoy.\n")

for i in range(1, TOTAL_CLIENTES + 1):
    print(f"--- Cliente {i} de {TOTAL_CLIENTES} ---")

    nombre = input("Nombre: ").strip()

    servicio = ""
    while servicio not in servicios_validos:
        servicio = input("Servicio (corte / cepillado / tintura): ").strip().lower()
        if servicio not in servicios_validos:
            print(" Servicio no válido.")

    valor = 0
    while valor <= 0:
        try:
            valor = float(input("Valor pagado: $"))
            if valor <= 0:
                print("   Debe ser mayor a 0.")
        except ValueError:
            print("   Ingrese un número válido.")

    conteo_servicios[servicio] += 1
    total_dia += valor
    print(f"  ✔ {nombre} — {servicio}: ${valor:,.0f}\n")

servicio_top = max(conteo_servicios, key=conteo_servicios.get)

print("=" * 45)
print("         RESUMEN DE LA JORNADA")
print("=" * 45)
print(f"  Total del día : ${total_dia:,.0f}")
for serv, cant in conteo_servicios.items():
    print(f"  {serv.capitalize():12}: {cant} cliente(s)")
print(f"\n   Más solicitado: {servicio_top} ({conteo_servicios[servicio_top]} veces)")
print("=" * 45)
