from user import User


class InMemoryRepository:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(User(item[0], item[1], item[2]))
    # TODO: Implementa los metodos get, update, delete, delete ... Los que te puedan hacer falta...
    def add_all(self, item):
        for i in item:
            if type(i) != list :
                self.data.append(User(i[0], i[1], i[2]))
            else:
                for j in i:
                    if type(i) != list:
                        self.data.append(User(j[0], j[1], j[2]))




