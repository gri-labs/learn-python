# TODO Crea una clase llamada Pelicula con las propiedades titulo, director, año, genero, clasificacion_por_edad y duracion.
# TODO Crea un método en la clase Pelicula llamado get_info() que devuelva la información de la película.
# TODO Crea una instancia de la clase Pelicula y asigna los valores "El Padrino", "Francis Ford Coppola",
# 1972, Crimen, R, 175 minutos a las propiedades titulo, director, ano, genero, clasificacion_por_edad y duracion.
# TODO Imprime la información de la película.


class Film:
    def __init__(self):
        self.title = ""
        self.director = ""
        self.year = 0
        self.genre = ""
        self.classification = ""
        self.duration = 0

    def get_info(self):
        print("Title: ", self.title)
        print("Director: ", self.director)
        print("Year: ", self.year)
        print("Genre: ", self.genre)
        print("Classification: ", self.classification)
        print("Duration: ", self.duration)


film = Film()
film.title = "El Padrino"
film.director = "Francis Ford Coppola"
film.year = 1972
film.genre = "Crimen"
film.classification = "R"
film.duration = 175
film.get_info()
