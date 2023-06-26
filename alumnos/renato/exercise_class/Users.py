class Users:
    def __init__(self, name, age, last_name):
        self.name = name
        self.age = age
        self.last_name = last_name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_lastname(self):
        return self.last_name

newUser = Users("Renato", 23, "Acciardi")

print(newUser.get_name())
print(newUser.get_age())
print(newUser.get_lastname())

# Instancia la clase Users
# Usa el metodo get_name
# Usa el metodo get_age
# Imprime el resultado de los metodos
# Implementa el metodo get_last_name
