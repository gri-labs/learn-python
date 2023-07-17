# Que es la clase InMemoryRepository?
# Es una clase que se encarga de obtener, guardar... datos en memoria
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

    # Actualiza un item de la lista data
    def update(self, id, item):
        self.data[id] = item

    # Borra un item de la lista data
    def delete(self, id):
        del self.data[id]


if __name__ == '__main__':
    print("Enjoy!")
    # TODO: Create a new instance of InMemoryRepository

    in_memory_repository = InMemoryRepository()
    # TODO: Add 1 movie to the repository with the following data:


def print_position(in_memory_repository):
    movies_position = input("Insert a position: ")
    get_position = in_memory_repository.get(movies_position)

    if get_position:
        for key, value in movies_position.items():
            print(value, key, get_position)

    movies = {
        'id': 1,
        'name': 'Star Wars'
    }
    in_memory_repository.add(movies)
    print_position(in_memory_repository)

    # TODO: Add 3 movies to the repository with the following data:

    movies = [
        {
            'id': 2,
            'name': 'Star Trek'
        },
        {
            'id': 3,
            'name': 'The Lord of the Rings'
        }
    ]

    in_memory_repository.add(movies)
    print_position()


    # TODO: Implementa una clase para printar los datos de un item
    # TODO: Print the movie with id 1
    # TODO: Print the movie with id 2
    # TODO: Print the movie with id 3

    # TODO: Update the movie with id 2 with the following data:
    # example
    # id: 2, name: Star Trek: The Next Generation
    # TODO: Print the movie with id 2
    # TODO: Delete the movie with id 1
    # TODO: Print all the movies
