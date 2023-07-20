from repository import InMemoryRepository
from print_data import PrintData

if __name__ == '__main__':
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()

    # TODO: Create a new instance of PrintData
    print_data_instance = PrintData()

    # TODO: Add array with multiple tuples to the repository
    movies = [
        {
            'id': 1,
            'name': 'Star Wars'
        },
        {
            'id': 2,
            'name': 'Star Trek'
        },
        {
            'id': 3,
            'name': 'The Lord of the Rings'
        }
    ]
    in_memory_repository.add_all(movies)

    # TODO: Print the movies
    all_movies = in_memory_repository.get_all()
    print_data_instance.print_data(all_movies)

    # TODO: Update the movie with id 2
    movie_update = {
        'id': 2,
        'name': 'Star Trek: The Next Generation'
    }
    in_memory_repository.update(1, movie_update)

    # TODO: Print the movies
    all_movies_updated = in_memory_repository.get_all()
    print_data_instance.print_data(all_movies_updated)

