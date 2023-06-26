#Ejercicio 2:
# Copia el archivo class song y users dentro de la carpeta exercise_class
# Termina las implementaciones que se piden en esos archivos
# Genera una nueva PR


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

lyrics = [' lalalalala\n lalalalalalalalala\n lalall lalalal lalalal']
my_song = Song(lyrics)

my_song.sing_me_a_song()