class Users:
    def __init__(self, name, age, last_name):
        self.name = name
        self.age = age
        self.last_name = last_name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_last_name(self):
        return self.last_name


# Instancia la clase Users
# Usa el metodo get_name
# Usa el metodo get_age
# Imprime el resultado de los metodos
# Implementa el metodo get_last_name

Alex = Users("Alex", 33, "Larrinaga")
name = Alex.get_name()
age = Alex.get_age()
last_name = Alex.get_last_name()
print(name), print(age), print(last_name)