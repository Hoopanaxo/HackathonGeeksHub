def cuadrado(x):
    return x**2

def cubo(x):
    return x**3

for valor in (1,2,3,4):
    if(valor % 2 == 0):
        print(f"Par:{valor}, Cuadrado: {cuadrado(valor)}")
    else:
        print(f"Impar: {valor}, Cubo: {cubo(valor)}")