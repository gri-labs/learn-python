class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


# Instancia la clase Song
# Usa el metodo sing_me_a_song

temazo = ["corazón", "latino", "mi", "sangre", "caliente", "pegada", "a", "tu", "piel"]
thing = Song(temazo)
thing.sing_me_a_song()
