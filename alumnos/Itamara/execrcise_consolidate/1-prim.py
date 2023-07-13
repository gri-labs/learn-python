# Determinar si un número entero proporcionado por el usuario es primo.
# Un número primo es un entero que no tiene más divisores que él mismo y la unidad.

num = int(input("Ingresa un número entero: "))

es_primo = True

if num <= 1:
    es_primo = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break

if es_primo:
    print(num, "es un número primo")
else:
    print(num, "no es un numero primo")
