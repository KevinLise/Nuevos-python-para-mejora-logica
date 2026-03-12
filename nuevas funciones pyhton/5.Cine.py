edad = int(input("ingrese sus edad: "))

if edad < 12:
    precio = 8000
elif edad <= 59:
    precio = 12000
    print
elif edad > 60:
    precio = 9000
    print("puede pasa sala de mayores")


print("total que debe pagar por la edad", precio)
