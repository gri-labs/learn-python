class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Instancia la clase Song
# Usa el metodo sing_me_a_song
song = Song([
    "Cancion 1",
    "Cancion 2",
    "Cancion 3"
])

song.sing_me_a_song()