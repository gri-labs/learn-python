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

# Clase para imprimir los datos de un item
class MoviePrinter:
    def print_movie(self, dictionary):
        for key, value in dictionary.items():
            print(key, value)


if __name__ == '__main__':

    print("Enjoy!")

    in_memory_repository = InMemoryRepository()

    # TODO: Add 1 movie to the repository with the following data:
    in_memory_repository.add({'id': 1, 'name': 'Star Wars'})

    # TODO: Add 3 movies to the repository with the following data:
    in_memory_repository.add_all([
        {'id': 2, 'name': 'Star Trek'},
        {'id': 3, 'name': 'The Lord of the Rings'}
    ])
    # TODO: Implementa una clase para printar los datos de un item
    movie_printer = MoviePrinter()
    # TODO: Print the movie with id 1
    result = in_memory_repository.get(0)
    movie_printer.print_movie(result)

    # TODO: Print the movie with id 2
    result = in_memory_repository.get(1)
    movie_printer.print_movie(result)

    # TODO: Print the movie with id 3
    result = in_memory_repository.get(2)
    movie_printer.print_movie(result)
    # TODO: Update the movie with id 2 with the following data:
    in_memory_repository.update(1, {'id': 2, 'name': 'Star Trek: The Next Generation'})

    # TODO: Print the movie with id 2
    result = in_memory_repository.get(1)
    movie_printer.print_movie(result)

    # TODO: Delete the movie with id 1
    in_memory_repository.delete(0)

    # TODO: Print all the movies
    for movie in in_memory_repository.data:
        movie_printer.print_movie(movie)
