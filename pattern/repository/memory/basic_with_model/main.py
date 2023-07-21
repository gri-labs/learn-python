from repository import InMemoryRepository
from print_data import PrintData

if __name__ == '__main__':
    # TODO: Instancia los objetos
    in_memory_repository = InMemoryRepository()
    print_data = PrintData()

    # TODO: añade un item al array

    item_user = (1, 'John Doe', 'john@gmail.com')
    in_memory_repository.add(item_user)

    user_with_id_one = in_memory_repository.get_by_id(1)

    print("User with id 1:")
    print_data.print_data(user_with_id_one)

    # TODO: añade un array de items al array

    item_user = [
        (2, 'John Doe 2', 'john@gmail.com'),
        (3, 'John Doe 3', 'john@gmail.com'),
        (4, 'John Doe 4', 'john@gmial.com')
    ]

    in_memory_repository.add_all(item_user)

    users = in_memory_repository.get_all()

    print("All users:")
    print_data.print_data(users)

    # TODO: selecciona un item del array y actualzia sus datos
    item_updated = (1, 'John Doe Updated', 'john@hotmail.com')
    in_memory_repository.update_by_id(1, item_updated)

    user_with_id_one = in_memory_repository.get_by_id(1)

    print("User with id 1 updated")
    print_data.print_data(user_with_id_one)

    # TODO: borra un item del array

    in_memory_repository.delete_by_id(1)

    users = in_memory_repository.get_all()

    print("User with id 1 deleted")
    print_data.print_data(users)

    # TODO: implementa el borrado de todos los datos de memoria

    in_memory_repository.delete_all()

    users = in_memory_repository.get_all()

    print("All data deleted")
    print_data.print_data(users)
