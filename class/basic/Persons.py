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


# Crear una instancia de la clase Person
person = Person()

# Establecer los atributos de la persona
person.set_name("John Doe")
person.set_age(25)
person.set_gender("Male")

# Mostrar la información de la persona
person.display_info()