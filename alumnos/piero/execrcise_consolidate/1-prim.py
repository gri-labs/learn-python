# Determinar si un número entero proporcionado por el usuario es primo.
# Un número primo es un entero que no tiene más divisores que él mismo y la unidad.

num=int(input("indicar un numero: "))
primo=True
for i in range(2,num):
    if (num%i) == 0:
        primo=False
if primo:
    print("es primo")
else:
    print("no es primo")