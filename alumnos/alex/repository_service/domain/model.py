import datetime
class StudentEntity():
    # Propiedades por defecto
    id = 0
    nombre = ""
    # TODO integrar el apellido en la entidad y en la persistencia
    apellido = ""
    # TODO integrar edad  en la entidad y en la persistencia
    edad = 0
    # TODO integrar el password en la entidad y en la persistencia
    password = ""
    def __init__(self, id=0, nombre="", apellido="", edad=0, password=""):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.password = password

    # TODO: Implementar un cambio de password
    def change_password(self, password):
        self.password = password

    def change_edad(self, edad):
        self.edad = edad


    # TODO: Implementa el nombre completo de los usuarios


    # TODO es mayor de edad?

    # TODO es menor de edad?

    # TODO cuantas estudiantes hay mayores de edad?

    # TODO cuantos estudiantes hay menores de edad?

