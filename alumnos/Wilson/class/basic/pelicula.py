# TODO Crea una clase llamada Pelicula con las propiedades titulo, director, año, genero, clasificacion_por_edad y duracion.
# TODO Crea un método en la clase Pelicula llamado get_info() que devuelva la información de la película.
# TODO Crea una instancia de la clase Pelicula y asigna los valores "El Padrino", "Francis Ford Coppola",
# 1972, Crimen, R, 175 minutos a las propiedades titulo, director, ano, genero, clasificacion_por_edad y duracion.
# TODO Imprime la información de la película.
class Pelicula:
    def __init__(self, titulo, director, año, genero, classificacion_por_edad, duracion):
        self.titulo = titulo
        self.director = director
        self.año = año
        self.genero = genero
        self.classificacion_por_edad = classificacion_por_edad
        self.duracion = duracion

    def get_info(self):
        info_pelicula = f"Pelicula: {self.titulo}, \n" \
                        f"Director: {self.director}, \n" \
                        f"Año: {self.año}, \n" \
                        f"Genero: {self.genero}, \n" \
                        f"Classificacion por edad: {self.classificacion_por_edad}, \n" \
                        f"Duración: {self.duracion}."
        return info_pelicula


if __name__ == '__main__':
    padrino = Pelicula("El Padrino", "Francis Ford Coppola", 1972, 'Crimen', 'R', '175 minutos')
    print(padrino.get_info())