class StudentEntity():
    # Propiedades por defecto
    id = 0
    nombre = ""
    apellido = ""
    password = ""

    def __init__(self, id=0, nombre="", apellido="", password=bytes()):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.password = password

    def generate_random_password(self, password):
        # TODO implement this method
        return password

    def full_name(self):
        # TODO: implement this method
        return ""
