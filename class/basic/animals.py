# Clase base (superclase) Animal
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        pass  # Este método se define en las clases hijas


# Clase derivada (subclase) Perro
class Perro:
    def __init__(self, animal):
        self.animal = animal

    def hablar(self):
        return self.animal.hablar()


animal = Animal("Pepito", 5)
perro = Perro(animal)

print(perro.hablar())
