# Ingresar un número y determinar si es par o impar
def par_impar(numero):
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"

numero = int(input("Ingresa un número: "))

print(par_impar(numero))
