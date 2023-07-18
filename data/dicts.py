# Que son los diccionarios?
# Los diccionarios son una estructura de datos que permite almacenar datos.
# Tres tipos de diccionarios:
# Diccionarios ordenados: estos diccionarios mantienen el orden en el que se agregan las claves.
# Ejemplo:

# Explica este diccionario
# clave uno, valor 1
# clave dos, valor 2
# clave tres, valor 3
dic = {'uno': 1, 'dos': 2, 'tres': 3}

# Diccionarios animados:
# Diccionarios anidados: estos diccionarios pueden contener otros diccionarios como claves o valores.

dic_anidado_one = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': {'cinco': 5, 'seis': 6, 'siete': 7}}

dic_animado_two = {1: {"a": "uno", "b": "dos"}, 2: {"a": "tres", "b": "cuatro"}}

# Diccionarios de objetos: estos diccionarios pueden contener funciones como claves o valores.
# Este diccionario contiene una función como clave y un valor como valor.

dic_objeto = {"nombre": "Juan", "apellido": "Perez"}

# Iterar en diccionarios

# Iterar en diccionarios ordenados
for key, value in dic.items():
    print(key, value)

# Iterar en diccionarios anidados
for key, value in dic_anidado_one.items():
    print(key, value)
    # Si el valor es un diccionario, iterar en el
    if isinstance(value, dict):
        for key, value in value.items():
            print(key, value)

# Iterar en diccionarios de objetos
for key, value in dic_objeto.items():
    print(key, value)
    if key == "nombre":
        print("Hola", value)


def hello():
    print("Hola")


dic_object_def = {"nombre": "Juan", "apellido": "Perez", "saludar": hello}

for key, value in dic_object_def.items():
    print(key, value)
    if key == "saludar":
        value()
    # Si el valor es una función, ejecutarla
    if callable(value):
        print("Es una función")
        value()


class Hello:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hola", self.name)


dict_object_class = {"nombre": "Juan", "apellido": "Perez", "saludar": Hello}

for key, value in dict_object_class.items():
    # Si el valor es una clase, lo instancia
    # Que es el type?
    # Es una clase que representa un tipo de dato
    if isinstance(value, type):
        # Si el valor de la clave es Juan, crea una instancia como Hello("Juan")
        print("Es una clase")
        value = value("Juan")
        value.hello()


# Ejercicio
# TODO: Crea un diccionario que asocie el nombre de cada país con su capital.
# TODO: Itera en el diccionario e imprime el nombre del país y su capital.

dictionary = {"Colombia": "Bogota", "Peru": "Lima", "Argentina": "Buenos Aires"}

for key, value in dictionary.items():
    print(key, value)