# Que es una tupla?
# Una tupla es una lista de elementos que no se puede modificar

# Ejemplo de tupla simple
tuple_one = (1, 2, 3, 4, 5)
print(type(tuple_one))

# Iterar en tupla simple
for i in tuple_one:
    print(i)

# Ejemplo de tupla anidada
tuple_anidado = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Iterar en tuplas anidadas
for i in tuple_anidado:
    for j in i:
        print(j)

# Ejemplo de tupla de diccionarios
tuple_diccionarios = ({"nombre": "Juan", "apellido": "Perez"}, {"nombre": "Pedro", "apellido": "Gomez"})
# Iterar en tuplas de diccionarios

for i in tuple_diccionarios:
    for key, value in i.items():
        print(key, value)


# Ejemplo de tupla de objetos
class Hello:
    def __init__(self, name):
        self.name = name


tuple_object = (Hello("Juan"), Hello("Pedro"))

# Iterar en tuplas de objetos
for i in tuple_object:
    print(i.name)


# Ejemplo de tupla de funciones

def hello():
    print("Hola")


tuple_funciones = (hello(), hello(), hello())

# Iterar en tuplas de funciones
for x in tuple_funciones:
    x

# Ejemplo de tupla de arrays

tuple_arrays = ([1, 2, 3], [4, 5, 6], [7, 8, 9])

# Iterar en tuplas de arrays
for i in tuple_arrays:
    for j in i:
        print(j)
