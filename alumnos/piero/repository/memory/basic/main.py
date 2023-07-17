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

class PrintMovie:
    def __init__(self, movie):
        self.movie= movie
    def print_data(self):
        print(self.movie)

if __name__ == '__main__':
    print("Enjoy!")
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()
    # TODO: Add 1 movie to the repository with the following data:
    # example
    # id: 1, name: Star Wars
    in_memory_repository.add({"id": 1, "name": "Star Wars"})
    # TODO: Add 3 movies to the repository with the following data:
    # example
    # id: 1, name: Star Wars
    # id: 2, name: Star Trek
    # id: 3, name: The Lord of the Rings
    in_memory_repository.add_all([
    {"id": 2, "name": "Star Trek"},
    {"id": 3, "name": "The Lord of the Rings"},
    {"id": 4, "name": "Interstellar"}
])
    # TODO: Implementa una clase para printar los datos de un item

    # TODO: Print the movie with id 1
    # TODO: Print the movie with id 2
    # TODO: Print the movie with id 3
    print_movie_1 = PrintMovie(in_memory_repository.get(0))
    print_movie_1.print_data()

    print_movie_2 = PrintMovie(in_memory_repository.get(1))
    print_movie_2.print_data()

    print_movie_3 = PrintMovie(in_memory_repository.get(2))
    print_movie_3.print_data()

    # TODO: Update the movie with id 2 with the following data:
    # example
    # id: 2, name: Star Trek: The Next Generation
    in_memory_repository.update(1,{"id": 2, "name": "Star Trek: The Next Generation"})
    # TODO: Print the movie with id 2
    print_movie_4 = PrintMovie(in_memory_repository.get(1))
    print_movie_4.print_data()
    # TODO: Delete the movie with id 1
    in_memory_repository.delete(0)
    # TODO: Print all the movies
    print_movie = PrintMovie(in_memory_repository.data)
    print_movie.print_data()
