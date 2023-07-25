from user import User


class InMemoryRepository:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(User(item[0], item[1], item[2]))

    # TODO: Implementa los metodos get, update, delete, delete ... Los que te puedan hacer falta...

    def add_all(self, items):
        for item in items:
            self.add(item)

    def get_all(self):
        return self.data

    def get_by_id(self, id):
        for user in self.data:
            if user.id == id:
                return user

    def update_by_id(self, id, item):
        for user in self.data:
            if user.id == id:
                user.name = item[1]
                user.email = item[2]
                return user

    def delete_by_id(self, id):
        for user in self.data:
            if user.id == id:
                self.data.remove(user)
                return user

    def delete_all(self):
        self.data.clear()
