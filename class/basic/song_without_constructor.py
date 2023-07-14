class Song:
    def sing_me_a_song(self, lyrics):
        for line in lyrics:
            print(line)


song = Song()
song.sing_me_a_song(["Happy birthday to you",
                     "I don't want to get sued",
                     "So I'll stop right there"])
