cafe = 4000
te = 3500
jugo = 5000

usuario = input("Ingrese su bebida (cafe / te / jugo): ")

if usuario == "cafe":
    cantidad = int(input("¿Cuántas unidades? "))
    total = cafe * cantidad
    print("Total a pagar $:", total)

elif usuario == "te":
    cantidad = int(input("¿Cuántas unidades? "))
    total = te * cantidad
    print("Total a pagar $:", total)

elif usuario == "jugo":
    cantidad = int(input("¿Cuántas unidades? "))
    total = jugo * cantidad
    print("Total a pagar $:", total)

else:
    print("Bebida no encontrada")
