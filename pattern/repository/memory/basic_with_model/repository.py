from user import User
from print_data import PrintData

# El repositorio InMemoryRepository
# Es una clase que se encarga de obtener datos y guardarlos en un array en memoria
# modelados por el item User
class InMemoryRepository:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(User(item[0], item[1], item[2]))

    # TODO: Implementa los metodos get, update, delete item, delete all


if __name__ == '__main__':
    repository = InMemoryRepository()
    print_users = PrintData()

    users = [
        ('1', 'ricardo', 'ricar@gmail.com')
    ]

    for i in users:
        repository.add(i)

    data = repository.data

    print("llamando a print_data")

    print_users.print_data(data)

    users_2 = [
        {
            '1',
            'ricardo',
            '',
        }
    ]

    for x in users_2:
        repository.add(x)

    # TODO: añade más datos al array items

    # TODO: selecciona un item del array items y actualiza sus datos

    # TODO: crea un nuevo array de datos

    # TODO: implementa el borrado de todos los datos de memoria
