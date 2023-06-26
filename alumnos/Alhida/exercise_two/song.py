class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

hungerGames = Song(["Are you, are you coming to the tree?\nWhen they strung up a man..."])


hungerGames.sing_me_a_song()