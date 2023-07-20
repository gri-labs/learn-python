from repository import InMemoryRepository
from print_data import PrintData

if __name__ == '__main__':
    print("Enjoy!")
    in_memory_repository = InMemoryRepository()

    # Add dictionary to array
    movie = {
        'id': 1,
        'name': 'Star Wars'
    }

    in_memory_repository.add(movie)

    # TODO: Print the movie with id 1

    movie_position_0 = in_memory_repository.get(0)
    print(movie_position_0)

    for key, value in movie_position_0.items():
        print("Printing keys and values from movie with id 1:")
        print("Key: ", key, "Value: ", value)

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
    print(movie_position_1)

    for key, value in movie_position_1.items():
        print(key, value)

    # TODO: Print the movie with id 3

    movie_position_2 = in_memory_repository.get(2)
    print(movie_position_2)

    for key, value in movie_position_2.items():
        print(key, value)

    # TODO: Print all the movies

    movies = in_memory_repository.get_all()

    for movie in movies:
        print(movie)

    # TODO: Update the movie with id 2 with the following data:

    movie_update = {
        'id': 2,
        'name': 'Star Trek: The Next Generation'
    }

    in_memory_repository.update(1, movie_update)

    # TODO: Print the movie with id 2

    movie_position_1_updated = in_memory_repository.get(1)
    print(movie_position_1_updated)

    for key, value in movie_position_1_updated.items():
        print(key, value)

    # TODO: Delete the movie with id 1

    in_memory_repository.delete(0)

    # TODO: Print all the movies
    result = in_memory_repository.get_all()

    for i in result:
        print("Final results: ")
        print("Type: ", type(i))
        for key, value in i.items():
            print(key, value)

    # TODO: Print with class PrintMovies
    # Instanciamos la clase PrintMovies
    print_movies = PrintData()

    # Llamamos al metodo print_data pasandole como parametro el resultado que es un array
    print("Printing array with class: ")
    print_movies.print_data(result)

    # Llamamos al metodo print_data pasandole como parametro el resultado que es un diccionario
    print("Printing dictionary with class: ")
    print_movies.print_data(movie_position_1_updated)
