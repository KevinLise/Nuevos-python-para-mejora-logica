counter = 0

for i in range(1, 6, 1):
    price = int(input("enter the price of product:"))
    if price > 100000:
        counter += 1
print("este el total de tu comprar", counter)
