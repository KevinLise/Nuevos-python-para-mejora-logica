edad = int(input("ingresa sus edad (para ver que grupo pertence):"))
if edad <= 13:
    print("no puedes ingresar al gym")
elif edad <= 17:
    print("puedes ingrese clase juvenil")
elif edad <= 59:
    print("puede entra clase general")
elif edad >= 60:
    print("puede entra clase senior")
else:
    ("no quien sabe a que grupo pertene")
