from repository import InMemoryRepository
from print_data import PrintData

if __name__ == '__main__':
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()

    # TODO: Create a new instance of PrintData
    print_data_instance = PrintData()

    # TODO: Add id, strings... with array format to the repository
    data_array = [
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
    in_memory_repository.add_all(data_array)

    # TODO: Delete the movie with id 2
    in_memory_repository.delete(1)

    # TODO: print all the ids
    all_movies = in_memory_repository.get_all()
    for movie in all_movies:
        print("Movie ID:", movie['id'])
