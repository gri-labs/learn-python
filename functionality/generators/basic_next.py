def funcion_generadora():
    for i in range(2):
        yield i


gen = funcion_generadora()
# Salida: 0
print(next(gen))
# Salida: 1
print(next(gen))
# Salida: StopIteration
print(next(gen))
