precio = 3.49
descuento = 1 - 0.6

precio_descontado = precio * descuento

numero_de_barras = int(input("Introduce el numero de barras vendidas: "))

print(f"Precio habitual: {precio}€")
print(f"Precio descontado: {precio*descuento}€")
print(f"Precio final: {precio_descontado * numero_de_barras} €")