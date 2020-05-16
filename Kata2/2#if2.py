edad = int(input("Edad?: "))
precio = 0

if edad < 4:
    pass
elif edad <= 18: #si es menor que 4 entra en el primer bloque
    # 4 <= edad <= 18  o edad > 4 and edad <= 18
    precio = 5
else: #mayores que 18
    precio = 10

print(f"Para tu edad: {edad} \nEl precio es: {precio}€")