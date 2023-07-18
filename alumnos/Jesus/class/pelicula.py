# TODO Crea una clase llamada Pelicula con las propiedades titulo, director, año, genero, clasificacion_por_edad y duracion.
# TODO Crea un método en la clase Pelicula llamado get_info() que devuelva la información de la película.
# TODO Crea una instancia de la clase Pelicula y asigna los valores "El Padrino", "Francis Ford Coppola",
# 1972, Crimen, R, 175 minutos a las propiedades titulo, director, ano, genero, clasificacion_por_edad y duracion.
# TODO Imprime la información de la película.
class Pelicula:
    def __init__(self, titulo, director, year, genero, clasificacion, duracion):
        self.titulo = titulo
        self.director = director
        self.year = year
        self.genero = genero
        self.clasificacion = clasificacion
        self.duracion = duracion

    def get_info(self):
        print("Titulo:", self.titulo)
        print("Director:", self.director)
        print("Año:", self.year)
        print("Genero:", self.genero)
        print("Clasificacion:", self.clasificacion)
        print("Duracion: ", self.duracion)


if __name__ == '__main__':
    # TODO: Crear un objeto de tipo Pelicula
    pelicula = Pelicula('El Padrino', 'Francis Ford Coppola', 1972, 'Crimen', 'R', 175)
    # TODO: Imprimir los valores
    pelicula.get_info()