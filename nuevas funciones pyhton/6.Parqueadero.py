horas = int(input("ingrese cuantas horas estubo parqueado: "))
if horas == 1:
    total = 5000

elif horas > 1:
    total = 5000 + (horas - 1) * 3000

else:
    ("horas invalidas")

print("el total de parqueo es:", total)
