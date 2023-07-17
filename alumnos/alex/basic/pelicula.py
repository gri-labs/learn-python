# TODO Crea una clase llamada Pelicula con las propiedades titulo, director, año, genero, clasificacion_por_edad y duracion.
# TODO Crea un método en la clase Pelicula llamado get_info() que devuelva la información de la película.
# TODO Crea una instancia de la clase Pelicula y asigna los valores "El Padrino", "Francis Ford Coppola",
# 1972, Crimen, R, 175 minutos a las propiedades titulo, director, ano, genero, clasificacion_por_edad y duracion.
# TODO Imprime la información de la película.

class Pelicula:

    def __init__(self, titulo, director, año, genero, clasificacion_por_edad, duracion):
        self.titulo = titulo
        self.director = director
        self.año = año
        self.genero = genero
        self.clasificacion_por_edad = clasificacion_por_edad
        self.duracion = duracion

    def get_info(self):
        print(self.titulo)
        print(self.director)
        print(self.año)
        print(self.genero)
        print(self.clasificacion_por_edad)
        print(self.duracion)

if __name__ == '__main__':
    el_padrino = Pelicula("El Padrino", "Francis Ford Coppola", "1972", "Crimen", "R", "175 minutos")
    el_padrino.get_info()