from main import InMemoryRepository
from main import PrintMovie


if __name__ == '__main__':
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()
    print_movie = PrintMovie(in_memory_repository.data)

    data_tuple = ((5, "Noseque movie"),)

    in_memory_repository.add_all(data_tuple)
    # TODO: Create a new instance of PrintData
    #print_movie_5 = PrintMovie(in_memory_repository)
    print_movie.print_data()
    # TODO: Add array with multiple tuples to the repository
    data_tuples = (
        (6, "Nosecuanto movie" ),
        (7, "Nosedonde movie")
    )
    
    in_memory_repository.add_all(data_tuples)
    # TODO: Print the movies
    for i in in_memory_repository.data:
        print(i)
 # Update the movie with id 6
    in_memory_repository.update(2, (6, "nuevo titulo"))

    for i in in_memory_repository.data:
        print(i)

