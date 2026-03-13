filas = int(input("Filas: "))
cols = int(input("Columnas: "))
matriz = []
for i in range(filas):
    fila = []
    for j in range(cols):
        valor = int(input(f"Elemento {i},{j}: "))
        fila.append(valor)
    matriz.append(fila)


# filas = 3
# columnas = 3
# matriz = []

# for i in range(filas):
#   fila = []
#  for j in range(columnas):
# Llenar con 0 o cualquier valor/cálculo
#     fila.append(0)
# matriz.append(fila)

# print(matriz)
