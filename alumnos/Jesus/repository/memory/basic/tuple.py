from repository import InMemoryRepository
from print_data import PrintData


if __name__ == '__main__':
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()

    # TODO: Create a new instance of PrintData
    print = PrintData()

    # TODO: Add array with multiple tuples to the repository
    movies = [
        {
            'id': 5,
            'name': 'Tiburón',
            'year': 1994
        },
        {
            'id': 6,
            'name': 'Matrix 2',
            'year': 1999
        }
    ]
    in_memory_repository.add_all(movies)

    # TODO: Print the movies
    print.print_data(in_memory_repository.get_all())

    # TODO: Update the movie with id 2
    movie2 = in_memory_repository.get(1)
    movie = {
        'id': 2,
        'name': 'El hombre sin pasado',
        'year': 1979
    }
    in_memory_repository.update(movie2, movie)

    # TODO: Print the movies
    print.print_data(in_memory_repository.get_all())
