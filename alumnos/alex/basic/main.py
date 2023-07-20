# Que es la clase InMemoryRepository?
# Es una clase que se encarga de obtener, guardar... datos en memoria
class InMemoryRepository:
    def __init__(self):
        # data es una variable privada
        # data es una lista
        self.data = []

    # Añade un item a la lista data
    def add(self, item):
        self.data.append(item)

    # Añade una lista de items a la lista data
    def add_all(self, items):
        self.data.extend(items)

    # Obtiene un item de la lista data
    def get(self, id):
        return self.data[id]

    # Actualiza un item de la lista data
    def update(self, id, item):
        self.data[id] = item

    # Borra un item de la lista data
    def delete(self, id):
        del self.data[id]

if __name__ == '__main__':
    print("Enjoy!")
    # TODO: Create a new instance of InMemoryRepository
    in_memory_repository = InMemoryRepository()

    # TODO: Add 1 movie to the repository with the following data:
    # example
    # id: 1, name: Star Wars
    star_wars = {'id': 1, 'name': 'Star Wars'}
    in_memory_repository.add(star_wars)
    # TODO: Add 3 movies to the repository with the following data:
    # example
    # id: 1, name: Star Wars
    # id: 2, name: Star Trek
    # id: 3, name: The Lord of the Rings

    item = [{'id': 2, 'name': 'Star Trek'},{'id': 3, 'name': 'The Lord of the rings'}]
    in_memory_repository.add_all(item)
    # TODO: Implementa una clase para printar los datos de un item
    # TODO: Print the movie with id 1
    print(in_memory_repository.get(0)['name'])


    # TODO: Print the movie with id 2
    print(in_memory_repository.get(1)['name'])

    # TODO: Print the movie with id 3
    print(in_memory_repository.get(2)['name'])

    # TODO: Update the movie with id 2 with the following data:
    # example
    # id: 2, name: Star Trek: The Next Generation
    in_memory_repository.update(2, {'id':3, 'name':'The Next Generation'})
    # TODO: Print the movie with id 2
    print(in_memory_repository.get(2))
    # TODO: Delete the movie with id 1
    in_memory_repository.delete(1)
    # TODO: Print all the movies

    for i in in_memory_repository.data:
        for key, value in i.items():
            print(value)

    dic = {'name':'Alex', 'age':33, 'gender':'man'}

    print(type(in_memory_repository.data))
    print(type(dic))

    lista = (1,2,3)
    print(type(lista))
