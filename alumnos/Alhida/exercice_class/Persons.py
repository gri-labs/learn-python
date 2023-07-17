class Person:
    def __init__(self):
        # Inicialización de variables
        self.name = ""
        self.age = 0
        self.gender = ""

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


if __name__ == '__main__':
    # TODO: Crear un objeto de tipo Person
    # TODO: Asignar valores a las variables
    # TODO: Imprimir los valores de las variables

    person = Person()
    person.set_name("Alhida")
    person.set_age(18)
    person.set_gender("Female")
    person.display_info()



