from repository import InMemoryRepository
from print_data import PrintData

if __name__ == '__main__':
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()

    # TODO: Create a new instance of PrintData
    print_data = PrintData()
    # TODO: Add id, strings... with array format to the repository
    in_memory_repository.add_all([
        {"id": 1, "name": "Star Wars"},
        {"id": 2, "name": "Star Trek"},
        {"id": 3, "name": "The Lord of the Rings"},
    ])
    # TODO: Delete the movie with id 2
    in_memory_repository.delete(2)
    # TODO: print all the ids
    print_data.print_data(in_memory_repository.get_all())