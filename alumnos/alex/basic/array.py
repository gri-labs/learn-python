from main import InMemoryRepository
from print_data import PrintData

if __name__ == '__main__':
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()
    # TODO: Create a new instance of PrintData
    print_data = PrintData()
    # TODO: Add id, strings... with array format to the repository
    in_memory_repository.add_all([5, 'Alex', 7])
    print_data.print_array(in_memory_repository.data)

    # TODO: Delete the movie with id 2
    # TODO: print all the ids