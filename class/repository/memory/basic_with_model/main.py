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

    def list(self):
        return self._data

    # TODO: Implementa los metodos get, update, delete item, delete all


if __name__ == '__main__':
    repository = InMemoryRepository()

    # Tenemos un array de datos
    users = [
        ('1', 'ricardo', 'ricar@gmail.com')
    ]

    # Recorremos el array de datos y por cada dato añadimos un item
    # al array _data
    for i in users:
        repository.add(i)

    # Recorremos el array _data y por cada item imprimimos sus datos
    for i in repository.list():
        print(i.id, i.name, i.email)

    # TODO añade más datos al array items

    # TODO selecciona un item del array items y actualiza sus datos

    # TODO crea un nuevo array de datos

    # TODO implementa el borrado de todos los datos de memoria
