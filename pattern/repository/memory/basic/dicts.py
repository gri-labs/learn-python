from repository import InMemoryRepository
from print_data import PrintData

if __name__ == '__main__':
    print("Enjoy!")
    in_memory_repository = InMemoryRepository()
    print_results = PrintData()

    # Add dictionary to array
    movie = {
        'id': 1,
        'name': 'Star Wars'
    }

    in_memory_repository.add(movie)

    # TODO: Print the movie with id 1

    movie_position_0 = in_memory_repository.get(0)

    print_results.print_data(movie_position_0)

    # TODO: Add 2 movies to the repository with the following data:
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

    in_memory_repository.add_all(movies)

    # TODO: Print the movie with id 2

    movie_position_1 = in_memory_repository.get(1)

    print_results.print_data(movie_position_1)

    # TODO: Print the movie with id 3

    movie_position_2 = in_memory_repository.get(2)

    print_results.print_data(movie_position_2)

    # TODO: Print all the movies

    movies = in_memory_repository.get_all()

    print_results.print_data(movies)

    # TODO: Update the movie with id 2 with the following data:

    movie_update = {
        'id': 2,
        'name': 'Star Trek: The Next Generation'
    }

    in_memory_repository.update(1, movie_update)

    # TODO: Print the movie with id 2

    movie_position_1_updated = in_memory_repository.get(1)

    print_results.print_data(movie_position_1_updated)

    # TODO: Delete the movie with id 1

    in_memory_repository.delete(0)

    # TODO: Print all the movies
    result = in_memory_repository.get_all()

    print_results.print_data(result)