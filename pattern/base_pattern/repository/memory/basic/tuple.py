from repository import InMemoryRepository
from print_data import PrintData


if __name__ == '__main__':
    in_memory_repository = InMemoryRepository()
    print_data = PrintData()
    movie = (1, 'The Shawshank Redemption', 1994, 'Frank Darabont')
    in_memory_repository.add(movie)
    result = in_memory_repository.get(0)
    print(type(result))
    print_data.print_data(result)
    movie_updated = (1, 'The Godfather', 1972, 'Francis Ford Coppola')
    in_memory_repository.update(0, movie_updated)
    result_updated = in_memory_repository.get(0)
    print(type(result_updated))
    print_data.print_data(result_updated)

