# ============================================================
# Ejercicio 18: Centro de idiomas - Evaluación de estudiantes
# ============================================================

bajo = medio = alto = 0
suma_promedios = 0
mejor_nombre = ""
mejor_promedio = -1
num_estudiantes = 0

print("=" * 45)
print("    CENTRO DE IDIOMAS ENGLISH PLUS 🌐")
print("=" * 45)
print("Escriba 'fin' en el nombre para terminar.\n")

while True:
    nombre = input("Nombre del estudiante (o 'fin'): ").strip()
    if nombre.lower() == "fin":
        break

    num_estudiantes += 1
    print(f"\n--- {nombre} ---")

    notas = []
    for materia in ("speaking", "listening", "reading"):
        nota = -1
        while not (0 <= nota <= 100):
            try:
                nota = float(input(f"  Nota {materia} (0-100): "))
                if not (0 <= nota <= 100):
                    print("  ⚠ Debe estar entre 0 y 100.")
            except ValueError:
                print("  ⚠ Ingrese un número válido.")
        notas.append(nota)

    promedio = sum(notas) / 3
    suma_promedios += promedio

    if promedio < 60:
        nivel = "bajo"
        bajo += 1
    elif promedio < 80:
        nivel = "medio"
        medio += 1
    else:
        nivel = "alto"
        alto += 1

    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_nombre  = nombre

    print(f"  ✔ Promedio: {promedio:.1f} → nivel {nivel}\n")

if num_estudiantes == 0:
    print("No se registraron estudiantes.")
else:
    promedio_grupo = suma_promedios / num_estudiantes
    print("=" * 45)
    print("        RESULTADOS DEL GRUPO")
    print("=" * 45)
    print(f"  Estudiantes registrados: {num_estudiantes}")
    print(f"  Promedio general       : {promedio_grupo:.1f}")
    print(f"  ⭐ Mejor estudiante    : {mejor_nombre} ({mejor_promedio:.1f})")
    print(f"  Nivel bajo  (< 60)     : {bajo}")
    print(f"  Nivel medio (60-79)    : {medio}")
    print(f"  Nivel alto  (80+)      : {alto}")
    print("=" * 45)
