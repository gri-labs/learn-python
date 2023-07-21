from repository import InMemoryRepository
from print_data import PrintData

if __name__ == '__main__':
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()
    # TODO: Create a new instance of PrintData
    print_data = PrintData()
    # TODO: Add id, strings... with array format to the repository
    ids = [1, 2, 3]

    in_memory_repository.add(ids)

    ids_updated = [4, 5]

    in_memory_repository.add_all(ids_updated)
    # TODO: print all the ids
    result = in_memory_repository.get_all()
    print_data.print_data(result)
