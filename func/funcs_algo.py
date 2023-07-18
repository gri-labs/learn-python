# La función recibe dos parametros y los imprime
# Al printar usa el placeholder  %r
# un placeholder es un marcador de posición
def print_two_again(arg1, arg2):
    print("arg1: %s, arg2: %s" % (arg1, arg2))


def print_one(arg1):
    print("arg1: %s" % arg1)


def print_none():
    print("Nothing...")


print_two_again("Zed", "Shaw")
print_one("¡Primero!")
print_none()


# Que es una funcion?
# Es un bloque de código que se ejecuta cuando se llama
# Y su función es realizar una tarea especifica
# La función recibe dos parametros y los imprime
# Al printar usa el placeholder  %d
# que es el placeholder %d?
# Es un marcador de posición para un número entero
def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b


def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b


def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b


edad = add(30, 5)
altura = subtract(78, 4)
peso = multiply(90, 2)
ci = divide(100, 2)

print("Edad: %d, Altura: %d, Peso: %d, CI: %d" % (edad, altura, peso, ci))

print("Aquí hay un acertijo.")
resultado = add(edad, subtract(altura, multiply(peso, divide(ci, 2))))
print("Eso se convierte en: ", resultado, "¿Puedes hacerlo a mano?")
