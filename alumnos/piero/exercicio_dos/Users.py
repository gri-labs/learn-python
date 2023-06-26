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

usuario = Users("Piero", 150, "Gio")

nombre = usuario.get_name()

edad = usuario.get_age()

apellido = usuario.get_last_name()

print(f'me llamo {nombre}, tengo {edad} años, y mi apellido es {apellido}')