# Ingresar un número y determinar si es par o impar
def es_par(numero):
    return numero % 2 == 0


numero = int(input("Ingresa un número: "))
if es_par(numero):
    print(numero, "es un número par")
else:
    print(numero, "no es un número par")
