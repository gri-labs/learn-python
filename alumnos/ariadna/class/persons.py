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

    persona = Person()

    persona.set_name('Maria')
    persona.set_age(25)
    persona.set_gender('Female')

    persona.display_info()