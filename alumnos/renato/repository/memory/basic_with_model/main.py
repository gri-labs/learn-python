# La clase User ( modelo ) es un item que guardamos en memoria
# a partir del repositorio InMemoryRepository
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email


# El repositorio InMemoryRepository
# Es una clase que se encarga de obtener datos y guardarlos en un array en memoria
# modelados por el item User
class InMemoryRepository:
    def __init__(self):
        self._data = []

    def add(self, item):
        self._data.append(User(item[0], item[1], item[2]))

    # TODO: Implementa los metodos get, update, delete item, delete all
