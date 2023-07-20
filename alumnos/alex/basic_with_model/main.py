from print_data import PrintData
from repository import InMemoryRepository

if __name__ == '__main__':
    # TODO: Instancia los objetos
    print_data = PrintData()
    repository = InMemoryRepository()
    # TODO: añade un item al array
    repository.add([1, 'Alex', 'alex@gmail.com'])
    # TODO: añade un array de items al array
    repository.add([[2, 'Ricardo', 'ricardo@gmail.com'], [3, 'Jesus', 'jesus@gmail.com']])
    # TODO: selecciona un item del array y actualiza sus datos
    item = [4,'Piero', 'piero@gmail.com']
    repository.data[1][1] = item
    # TODO: borra un item del array

    # TODO: implementa el borrado de todos los datos de memoria
