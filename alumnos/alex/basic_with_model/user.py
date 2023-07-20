# La clase User ( modelo ) es un item que guardamos en memoria
# a partir del repositorio InMemoryRepository
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email