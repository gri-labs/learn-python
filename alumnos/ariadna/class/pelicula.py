class Pelicula:
    def __init__(self, titulo, director, ano, genero, clasificacion_por_edad, duracion):
        self.titulo = titulo
        self.director = director
        self.ano = ano
        self.genero = genero
        self.clasificacion_por_edad = clasificacion_por_edad
        self.duracion = duracion

    def get_info(self):
        print("Título:", self.titulo)
        print("Director:", self.director)
        print("Año:", self.año)
        print("Género:", self.genero)
        print("Clasificación por edad:", self.clasificacion_por_edad)
        print("Duración:", self.duracion)


if __name__ == '__main__':

    pelicula = Pelicula("El Padrino", "Francis Ford Coppola", 1972, "Crimen", "R", "175 minutos")

    pelicula.get_info()