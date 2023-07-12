# Los terminos de la serie de Fibonacci son 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Cada termino de la serie de Fibonacci es la suma de los dos terminos anteriores.
# Escriba un programa que genere los primeros n terminos de la serie de Fibonacci.
# Donde n es un valor que el usuario ingresara por teclado.

numero= int(input("indica el numero: "))
num1 = 0
num2 = 1

lista = [num1, num2]

for i in range(2, numero):
    num3 = num1 + num2
    lista.append(num3)
    num1 = num2
    num2 = num3
    
print(lista)

