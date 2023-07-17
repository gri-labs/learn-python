# Que es la clase InMemoryRepository?
# Es una clase que se encarga de obtener, guardar... datos en memoria
class InMemoryRepository:
    def __init__(self):
        # .data es una variable privada
        # .data es una lista
        #
        self.data = []

    def add(self, item):
        self.data.append(item)

    def get(self, id):
        return self.data[id]

    def list(self):
        return self.data

    def update(self, id, item):
        self.data[id] = item

    def delete(self, id):
        del self.data[id]


if __name__ == '__main__':
    print("Enjoy!")
    # TODO: Crea una instancia de InMemoryRepository
    # TODO: Añade 3 peliculas
    # TODO: Imprime la lista de peliculas
    # TODO: Imprime la pelicula con id 1
    # TODO: Actualiza la pelicula con id 1
    # TODO: Elimina la pelicula con id 2
    # TODO: Imprime la lista de peliculas
