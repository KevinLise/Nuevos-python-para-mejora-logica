planes = {
    "basico"  : 50000,
    "premium" : 90000,
    "familiar": 130000
}

total_recaudado = 0
conteo_planes   = {"basico": 0, "premium": 0, "familiar": 0}
num_personas    = 0

print("=" * 45)
print("      CLUB RECREATIVO PARAÍSO ")
print("=" * 45)
print("Planes: básico $50,000 | premium $90,000 | familiar $130,000")
print("Escriba 'fin' en el nombre para terminar.\n")

while True:
    nombre = input("Nombre (o 'fin'): ").strip()
    if nombre.lower() == "fin":
        break

    edad = -1
    while edad < 0:
        try:
            edad = int(input("Edad: "))
            if edad < 0:
                print("  ⚠ No puede ser negativa.")
        except ValueError:
            print("  ⚠ Ingrese un número válido.")

    plan = ""
    while plan not in planes:
        plan = input("Plan (basico / premium / familiar): ").strip().lower()
        if plan not in planes:
            print("   Plan no válido.")

    valor = planes[plan]
    conteo_planes[plan] += 1
    total_recaudado += valor
    num_personas += 1

    # Mensajes especiales por edad
    if edad < 18:
        print(f"  ℹ  Registro juvenil")
    elif edad >= 60:
        print(f"  ℹ  Beneficio senior")

    print(f"  ✔ {nombre} — plan {plan}: ${valor:,}\n")

if num_personas == 0:
    print("No se registraron personas.")
else:
    plan_top = max(conteo_planes, key=conteo_planes.get)

    print("=" * 45)
    print("       RESUMEN DEL CLUB")
    print("=" * 45)
    print(f"  Personas registradas: {num_personas}")
    print(f"  Total recaudado     : ${total_recaudado:,}")
    for p, c in conteo_planes.items():
        print(f"  Plan {p.capitalize():10} : {c} persona(s)")
    print(f"\n   Plan más vendido: {plan_top} ({conteo_planes[plan_top]} veces)")
    print("=" * 45)
