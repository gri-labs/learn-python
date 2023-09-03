# Que es un array
# Un array es una lista de elementos

# Ejemplo de array simple
array_one = [1, 2, 3, 4, 5, 6]

# Iterar en array simple
for i in array_one:
    print(i)

# Ejemplo de array anidado
array_anidado = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Iterar en arrays anidados
for i in array_anidado:
    for j in i:
        print(j)

# Ejemplo de array de diccionarios
array_de_diccionarios = [{"nombre": "Juan", "apellido": "Perez"}, {"nombre": "Pedro", "apellido": "Gomez"}]

# Iterar en arrays de diccionarios
for i in array_de_diccionarios:
    for key, value in i.items():
        print(key, value)


# Ejemplo de array de objetos
class Hello:
    def __init__(self, name):
        self.name = name


array_de_objetos = [Hello("Juan"), Hello("Pedro")]

# Iterar en arrays de objetos
for i in array_de_objetos:
    print(i.name)


# Ejemplo de array de funciones

def hello():
    print("Hola")


array_de_funciones = [hello(), hello(), hello()]

# Iterar en arrays de funciones
for x in array_de_funciones:
    x

# Ejemplo de array de tuples
array_de_tuples = [(1, 2), (3, 4), (5, 6)]

# Iterar en arrays de tuples
for i in array_de_tuples:
    for j in i:
        print(j)
