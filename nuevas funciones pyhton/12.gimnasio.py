# ============================================================
# Ejercicio 12: Gimnasio - Promedio de rendimiento semanal
# ============================================================

TOTAL_PERSONAS = 5
bajo = medio = alto = 0

print("=" * 45)
print("        GIMNASIO FUERZA TOTAL 💪")
print("=" * 45)

for i in range(1, TOTAL_PERSONAS + 1):
    print(f"\n--- Persona {i} de {TOTAL_PERSONAS} ---")

    nombre = input("Nombre: ").strip()

    dias = -1
    while not (0 <= dias <= 7):
        try:
            dias = int(input("Días asistidos en la semana (0-7): "))
            if not (0 <= dias <= 7):
                print("  ⚠ Debe ser entre 0 y 7.")
        except ValueError:
            print("  ⚠ Ingrese un número válido.")

    minutos = -1
    while minutos < 0:
        try:
            minutos = int(input("Minutos promedio entrenados por día: "))
            if minutos < 0:
                print("  ⚠ No puede ser negativo.")
        except ValueError:
            print("  ⚠ Ingrese un número válido.")

    if dias < 3:
        nivel = "bajo compromiso"
        bajo += 1
    elif dias <= 4:
        nivel = "compromiso medio"
        medio += 1
    else:
        nivel = "compromiso alto"
        alto += 1

    print(f"  ✔ {nombre}: {dias} días, {minutos} min/día → {nivel}")

print("\n" + "=" * 45)
print("         RESUMEN DEL GIMNASIO")
print("=" * 45)
print(f"  Bajo compromiso  : {bajo} persona(s)")
print(f"  Compromiso medio : {medio} persona(s)")
print(f"  Compromiso alto  : {alto} persona(s)")
print("=" * 45)
