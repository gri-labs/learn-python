from user import User


class InMemoryRepository:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(User(item[0], item[1], item[2]))
    # TODO: Implementa los metodos get, update, delete, delete ... Los que te puedan hacer falta...
