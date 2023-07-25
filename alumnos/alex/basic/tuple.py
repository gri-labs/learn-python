from main import InMemoryRepository
from print_data import PrintData

if __name__ == '__main__':
    # TODO: Create a new instance of InMemoryRepository
    repository = InMemoryRepository()
    # TODO: Create a new instance of PrintData
    print_data = PrintData()
    # TODO: Add array with multiple tuples to the repository
    array = [(1,2,3), ({'título': 'El Señor de los Anillos', 'género': 'ciencia ficción', 'duración': 200}, 'Javier')]
    repository.add_all([array])
    # TODO: Print the movies
    print_data.print_data(repository.data)
    # TODO: Update the movie with id 2

    # TODO: Print the movies

