from user import User


# El repositorio InMemoryRepository
# Es una clase que se encarga de obtener datos y guardarlos en un array en memoria
# modelados por el item User
class InMemoryRepository:
    def __init__(self):
        self.data = []

    def add_one(self, item):
        self.data.append(User(item[0], item[1], item[2]))

    def add_many(self, items):
        for item in items:
            self.add_one(item)

    def get_one_by_id(self, id):
        return self.data[int(id)]

    def get_all(self):
        return self.data

    def update_one(self, id, item):
        self.data[int(id)] = User(int(id), item[0], item[1])

    def delete_one(self, id):
        del self.data[int(id)]

    def delete_all(self):
        self.data = []
