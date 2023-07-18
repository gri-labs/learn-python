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


class display_movie:
    def print_movie(self, movie):
        print("Movie ID: {movie['id']}")
        print("Movie Name: {movie['name']}")


if __name__ == '__main__':
    print("Enjoy!")
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()

    # TODO: Add 1 movie to the repository with the following data:
    # example
    # id: 1, name: Star Wars
    movie1 = {'id': 1, 'name': 'Soy Leyenda'}
    in_memory_repository.add(movie1)

    # TODO: Add 3 movies to the repository with the following data:
    # example
    # id: 1, name: Star Wars
    # id: 2, name: Star Trek
    # id: 3, name: The Lord of the Rings
    movies = [
        {
            'id': 2,
            'name': 'bird box'

        },
        {
            'id': 3,
            'name': 'La guerra de los mundos'
        }
    ]
    in_memory_repository.add_all(movies)

    # TODO: Implementa una clase para printar los datos de un item


    # TODO: Print the movie with id 1
    # TODO: Print the movie with id 2
    # TODO: Print the movie with id 3
    displayMovie = display_movie()

    movie1 = in_memory_repository.get(0)
    displayMovie.print_movie(movie1)

    movie2 = in_memory_repository.get(1)
    displayMovie.print_movie(movie2)

    movie3 = in_memory_repository.get(2)
    displayMovie.print_movie(movie3)

    # TODO: Update the movie with id 2 with the following data:
    # example
    # id: 2, name: Star Trek: The Next Generation
    # TODO: Print the movie with id 2
    # TODO: Delete the movie with id 1
    # TODO: Print all the movies

    updated_movie2 = {'id': 2, 'name': 'Bird box: Barcelona'}
    in_memory_repository.update(1, updated_movie2)

    updated_movie2 = in_memory_repository.get(1)
    displayMovie.print_movie(updated_movie2)

    in_memory_repository.delete(0)

    all_movies = in_memory_repository.data
    for movie in all_movies:
        displayMovie.print_movie(movie)


