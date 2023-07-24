from user import User


class InMemoryRepository:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(User(item[0], item[1], item[2]))
    # TODO: Implementa los metodos get, update, delete, delete ... Los que te puedan hacer falta...
    def add_all(self, item):
        for i in item:
            if type(i) == list:
                self.add(i)
            else:
                for j in i:
                    if type(i) != list:
                        self.add(j)




