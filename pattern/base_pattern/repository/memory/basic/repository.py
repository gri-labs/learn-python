# Que es la clase InMemoryRepository?
# Es una clase que se encarga de obtener, guardar... datos en memoria

from print_data import PrintData


class InMemoryRepository:
    def __init__(self):
        # data es una variable privada
        # data es una lista
        self.data = []

    # Añade un elemento a la lista data en la última posición
    def add(self, item):
        self.data.append(item)

    # Añade todos los elementos de un array a la lista data
    def add_all(self, items):
        self.data.extend(items)

    # Obtiene un item de la lista data
    def get(self, id):
        return self.data[id]

    def get_all(self):
        return self.data

    # Actualiza un item de la lista data
    def update(self, id, item):
        self.data[id] = item

    # try to update a tuple of array
    def update_tuple(self, id, item):
        self.data[id] = item

    # Borra un item de la lista data
    def delete(self, id):
        del self.data[id]
