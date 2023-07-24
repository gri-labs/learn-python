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

    def get_all(self):
        return self.data

    # Actualiza un item de la lista data
    def update(self, id, item):
        self.data[id] = item

    # Borra un item de la lista data
    def delete(self, id):
        del self.data[id]

class Print:
    def print_item(self, item):
        if isinstance(item, dict):
            for key, value in item.items():
                print(key, value)


if __name__ == '__main__':
    print("Enjoy!")
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()
    # TODO: Add 1 movie to the repository with the following data:
    # example
    # id: 1, name: Star Wars
    movie = {
        'id': 1,
        'name': 'Matrix'
    }
    in_memory_repository.add(movie)

    # TODO: Add 3 movies to the repository with the following data:
    # example
    # id: 1, name: Star Wars
    # id: 2, name: Star Trek
    # id: 3, name: The Lord of the Rings
    movies = [
        {
            'id': 2,
            'name': 'Star Trek'
        },
        {
            'id': 3,
            'name': 'Otra peli'
        },
        {
            'id': 4,
            'name': 'Otra peli parte 2'
        }
    ]
    in_memory_repository.add_all(movies)

    # TODO: Implementa una clase para printar los datos de un item
    print_data = Print()

    # TODO: Print the movie with id 1
    movie_position_1 = in_memory_repository.get(0)
    print_data.print_item(movie_position_1)

    # TODO: Print the movie with id 2
    movie_position_2 = in_memory_repository.get(1)
    # for key, value in movie_position_2.items():
    #   print(key, value)
    print_data.print_item(movie_position_2)

    # TODO: Print the movie with id 3
    movie_position_3 = in_memory_repository.get(2)
    # for key, value in movie_position_3.items():
    #   print(key, value)
    print_data.print_item(movie_position_3)

    # TODO: Update the movie with id 2 with the following data:
    # example
    # id: 2, name: Star Trek: The Next Generation
    movie_update = {
        'id': 2,
        'name': 'The Next Generation'
    }
    in_memory_repository.update(2, movie_update)
    
    # TODO: Print the movie with id 2
    print_movie_2 = in_memory_repository.get(1)
    # print(type(print_movie_2))
    # for key, value in print_movie_2.items():
    #   print(key, value)
    print_data.print_item(print_movie_2)

    # TODO: Delete the movie with id 1
    del_movie_1 = in_memory_repository.get(0)
    del_movie_1.delete(del_movie_1)

    # TODO: Print all the movies
    movies = in_memory_repository.get_all()
    print_data.print_item(movies)
    # for i in movies:
    #    print("Type: ", type(i))
    #    for key, value in i.items():
    #        print(key, value)
