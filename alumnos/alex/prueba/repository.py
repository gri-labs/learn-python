class InMemoryRepository:
    def __init__(self):
        # data es una variable privada
        # data es una lista
        self.data = []

    # Añade un item a la lista data
    def add(self, item):
        self.data.append(item)

    # Añade una lista de items a la lista data
    def add_all(self, items):
        self.data.extend(items)

    # Obtiene un item de la lista data
    def get(self, id):
        return self.data[id]

    def get_all(self):
        return self.data

    # Actualiza un item de la lista data
    def update(self, id, item):
        self.data[id] = item

    # Borra un item de la lista data
    def delete(self, id):
        del self.data[id]


if __name__ == '__main__':

    repo = InMemoryRepository()
    """repo.add([1,2,3])
    repo.add_all([1,2,3])"""
    repo.add_all(1)
    print(repo.add_all(1))
    """for i in repo.get_all():
        print(type(i))"""


