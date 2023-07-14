# TODO Crea una clase llamada Pelicula con las propiedades titulo, director, año, genero, clasificacion_por_edad y duracion.
# TODO Crea un método en la clase Pelicula llamado get_info() que devuelva la información de la película.
# TODO Crea una instancia de la clase Pelicula y asigna los valores "El Padrino", "Francis Ford Coppola",
# 1972, Crimen, R, 175 minutos a las propiedades titulo, director, ano, genero, clasificacion_por_edad y duracion.
# TODO Imprime la información de la película.

class Pelicula:
    def __init__(self, titulo, director, ano, genero, clasificacion_por_edad, duracion):
        self.titulo = titulo
        self.director = director
        self.ano = ano
        self.genero = genero
        self.clasificacion_por_edad = clasificacion_por_edad
        self.duracion = duracion

    def get_info(self):
        return [self.titulo, self.director, self.ano, self.genero, self.clasificacion_por_edad, self.duracion]


if __name__ == '__main__':
    film = Pelicula("El Padrino", "Francis Ford Coppola", 1972, "Crimen", "R", "175 minutos")
    print(film.get_info())
