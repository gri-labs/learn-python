class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

mySong = Song(["This is my song",
               "This is another line"])

Song.sing_me_a_song(mySong)

# Instancia la clase Song
# Usa el metodo sing_me_a_song
