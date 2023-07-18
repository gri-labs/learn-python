from repository import InMemoryRepository
from print_data import PrintData

if __name__ == '__main__':
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()
    # TODO: Create a new instance of PrintData
    print_data = PrintData()
    # TODO: Add array with multiple tuples to the repository
    in_memory_repository.add_all([
        (1, "Star Wars"), (2, "Star Trek"), (3, "The Lord of the Rings")
    ])
    # TODO: Print the movies
    print_data.print_data(in_memory_repository.get_all())
    # TODO: Update the movie with id 2
    in_memory_repository.update(1, (2, "Star Trek: Next Generation"))
    # TODO: Print the movies
    print_data.print_data(in_memory_repository.get_all())
