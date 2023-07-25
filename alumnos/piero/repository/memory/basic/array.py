from main import InMemoryRepository
from main import PrintMovie


if __name__ == '__main__':
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()
    print_movie = PrintMovie(in_memory_repository.data)

    data_new = [
        [1, "Some other movie"]
    ]
    in_memory_repository.add_all(data_new)
    # TODO: Create a new instance of PrintData
    #print_movie_4 = PrintMovie(in_memory_repository.get(0))
    print_movie.print_data()
    # TODO: Add id, strings... with array format to the repository
    data_list = [
        [2, "Some movie"],
        [3, "Another movie"],
        [4, "One more movie"]
    ]
    in_memory_repository.add_all(data_list)
    # TODO: Delete the movie with id 2
    in_memory_repository.delete(2)
    # TODO: print all the ids
    print("IDs de las películas:")
    for item in in_memory_repository.data:
        if isinstance(item, list):
            print(item[0])