# ============================================================
# Ejercicio 14: Cine - Control de sala
# ============================================================

print("=" * 45)
print("        CINE LUNA PLATEADA 🎬")
print("=" * 45)

capacidad = 0
while capacidad <= 0:
    try:
        capacidad = int(input("Capacidad total de la sala: "))
        if capacidad <= 0:
            print("  ⚠ Debe ser mayor a 0.")
    except ValueError:
        print("  ⚠ Ingrese un número válido.")

ninos = adultos = adultos_mayores = 0
personas_ingresadas = 0

print(f"\nRegistrando ingreso (máximo {capacidad} personas).\n")

while personas_ingresadas < capacidad:
    print(f"--- Persona {personas_ingresadas + 1} ---")
    opcion = input("¿Registrar persona? (s/n): ").strip().lower()
    if opcion != "s":
        break

    edad = -1
    while edad < 0:
        try:
            edad = int(input("Edad: "))
            if edad < 0:
                print("  ⚠ La edad no puede ser negativa.")
        except ValueError:
            print("  ⚠ Ingrese un número válido.")

    if edad < 12:
        categoria = "niño"
        ninos += 1
    elif edad < 60:
        categoria = "adulto"
        adultos += 1
    else:
        categoria = "adulto mayor"
        adultos_mayores += 1

    personas_ingresadas += 1
    print(f"  ✔ Registrado como: {categoria}\n")

sala_llena = "Sí ✔" if personas_ingresadas >= capacidad else "No ✗"

print("=" * 45)
print("         RESUMEN DE LA SALA")
print("=" * 45)
print(f"  Capacidad total      : {capacidad}")
print(f"  Total ingresados     : {personas_ingresadas}")
print(f"  Niños (< 12)         : {ninos}")
print(f"  Adultos (12-59)      : {adultos}")
print(f"  Adultos mayores (60+): {adultos_mayores}")
print(f"  ¿Sala llena?         : {sala_llena}")
print("=" * 45)
