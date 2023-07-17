# Los términos de la serie de Fibonacci son 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Cada término de la serie de Fibonacci es la suma de los dos términos anteriores.
# Escriba un programa que genere los primeros n términos de la serie de Fibonacci.
# Donde n es un valor que el usuario ingresará por teclado.

n = int(input("Ingresa el número de términos: "))

fibonacci = [0, 1]

while len(fibonacci) < n:
    next_num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_num)

print("Los primeros", n, "términos de la serie de Fibonacci son:", fibonacci)
