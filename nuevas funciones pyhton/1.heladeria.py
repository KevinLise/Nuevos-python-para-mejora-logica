vainilla = 0
chocolate = 0
fresa = 0

for i in range(0, 5, 1):
    cliente = input("ingrese el helado:")
    if cliente == "vainilla":
        vainilla += 1
    elif cliente == "chocolate":
        chocolate += 1
    elif cliente == "fresa":
        fresa += 1
print("repetiste es sabor vainilla :", vainilla)
print("repetiste es sabor chocolate:", chocolate)
print("repetiste es sabor fresa:", fresa)
