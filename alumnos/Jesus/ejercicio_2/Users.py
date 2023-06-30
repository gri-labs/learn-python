class Users:
    def __init__(self, name, age, last_name):
        self.name = name
        self.age = age
        self.last_name = last_name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


# Instancia la clase Users
# Usa el metodo get_name
# Usa el metodo get_age
# Imprime el resultado de los metodos
# Implementa el metodo get_last_name
usuario1 = Users("Jesus", 45, "RV")
print(usuario1.name, usuario1.last_name, usuario1.age)