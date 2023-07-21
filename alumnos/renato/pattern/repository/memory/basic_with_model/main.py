from print_data import PrintData
from repository import InMemoryRepository

if __name__ == '__main__':
    repository = InMemoryRepository()
    print_users = PrintData()

    repository.add_one(['0', 'Renato', 'rena@gmail.com'])
    print_users.print_data(repository.get_all())
    users_array = [
        ['1', 'Loida', 'loi@gmail.com'],
        ['2', 'Merlin', 'merl@gmail.com'],
    ]
    repository.add_many(users_array)
    print_users.print_data(repository.get_all())

    update_id = input('Dame el ID para cambiar: ')
    update_name = input('Dame el nuevo nombre: ')
    update_email = input('Dame el nuevo email: ')
    repository.update_one(update_id, [update_name, update_email])
    print_users.print_data(repository.get_all())

    delete_id = input('Dame el ID para eliminar: ')
    repository.delete_one(delete_id)
    print_users.print_data(repository.get_all())

    delete_all = input('Presiona enter para borrar todo')
    repository.delete_all()
    print_users.print_data(repository.get_all())
