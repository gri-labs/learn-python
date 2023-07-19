# Genera una pequeña aplicación, para registrar un usuario en memoria o base de datos. Tendrás que tener una clase en
# un fichero repository, donde haya diferentes métodos (add, get … ). La aplicación tendrá dos puntos de entrada:
# “/create/user” 🡪 Creación de usuario Ejemplo:
# POST 🡪 /créate/user/1/pepe/25 “/user/id”
# 🡪 Obtención de usuario
# Ejemplo:
# GET 🡪 /user/1
# Cuando llamamos al endpoint de creación de usuario, se tendrá que añadir en memoria el
# usuario o conectar con base de datos y hacer el respectivo INSERT, en la correspondiente tabla. Cuando llamamos al
# endpoint de obtención de usuario, el repositorio tendrá que devolvernos el usuario añadido anteriormente. Los
# atributos del usuario pueden ser: id, name, age .. (opcional)


class Repository:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name, age):
        self.users[user_id] = {'name': name, 'age': age}

    def get_user(self, user_id):
        return self.users.get(user_id)


