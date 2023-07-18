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

    def size_movies(self):
        return len(self.data)


class PrintMovie:
    def print_movie(self, item):
        if isinstance(item, dict):
            for key, movie in item.items():
                print(key, movie)


if __name__ == '__main__':
    print("Enjoy!")
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()
    # TODO: Add 1 movie to the repository with the following data:
    # example
    movies = {'id': 1, 'name': 'Star Wars'}
    in_memory_repository.add(movies)
    movies_tt = [{'id': 2, 'name': 'Star Trek'}, {'id': 3, 'name': 'The Lord of the Rings'}]
    in_memory_repository.add_all(movies_tt)
    # id: 1, name: Star Wars
    # TODO: Add 3 movies to the repository with the following data:
    # id: 3, name: The Lord of the Rings

    # TODO: Implementa una clase para printar los datos de un item
    # TODO: Print the movie with id 1
    # TODO: Print the movie with id 2
    # TODO: Print the movie with id 3

    # TODO: Update the movie with id 2 with the following data:
    # example
    in_memory_repository.update(1, 'Start Trek: Next Generation')
    # id: 2, name: Star Trek: The Next Generation
    # TODO: Print the movie with id 2
    impresora = PrintMovie()
    mov_two = in_memory_repository.get(2)
    impresora.print_movie(mov_two)
    # TODO: Delete the movie with id 1
    in_memory_repository.delete(0)
    # TODO: Print all the movies
    list_movies = in_memory_repository.get_all()
    print(list_movies)
    total_peliculas = in_memory_repository.size_movies()
    print(total_peliculas)
    for i in range(0, total_peliculas):
        mov = in_memory_repository.get(i)
        impresora.print_movie(mov)