TOTAL_VEHICULOS = 8
TARIFA_CARRO = 4000
TARIFA_MOTO  = 2000

total_recaudado = 0
carros = motos = 0
mejor_placa = ""
mayor_pago  = 0

print("=" * 45)
print("        PARQUEADERO SEGURO ")
print("=" * 45)
print(f"  Carro: ${TARIFA_CARRO:,}/hora  |  Moto: ${TARIFA_MOTO:,}/hora\n")

for i in range(1, TOTAL_VEHICULOS + 1):
    print(f"--- Vehículo {i} de {TOTAL_VEHICULOS} ---")

    placa = input("Placa: ").strip().upper()

    tipo = ""
    while tipo not in ("carro", "moto"):
        tipo = input("Tipo (carro / moto): ").strip().lower()
        if tipo not in ("carro", "moto"):
            print("   Solo 'carro' o 'moto'.")

    horas = 0
    while horas <= 0:
        try:
            horas = float(input("Horas parqueado: "))
            if horas <= 0:
                print("   Debe ser mayor a 0.")
        except ValueError:
            print("   Ingrese un número válido.")

    tarifa = TARIFA_CARRO if tipo == "carro" else TARIFA_MOTO
    pago = tarifa * horas

    if tipo == "carro":
        carros += 1
    else:
        motos += 1

    total_recaudado += pago

    if pago > mayor_pago:
        mayor_pago  = pago
        mejor_placa = placa

    print(f"   {placa} ({tipo}) — {horas}h → ${pago:,.0f}\n")

print("=" * 45)
print("       RESUMEN DEL PARQUEADERO")
print("=" * 45)
print(f"  Total recaudado : ${total_recaudado:,.0f}")
print(f"  Carros          : {carros}")
print(f"  Motos           : {motos}")
print(f"  Mayor pagador   : {mejor_placa} (${mayor_pago:,.0f})")
print("=" * 45)
