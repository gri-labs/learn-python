from repository import InMemoryRepository
from print_data import PrintData

if __name__ == '__main__':
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()

    # TODO: Create a new instance of PrintData
    print_data = PrintData()
    # TODO: Add id, strings... with array format to the repository
    in_memory_repository.add_all(
        [1, 2, 3, 4]
    )
    # TODO: Delete the movie with id 2
    in_memory_repository.delete(1)
    # TODO: print all the ids
    print_data.print_data(in_memory_repository.get_all())
