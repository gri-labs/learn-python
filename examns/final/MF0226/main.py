random

class :


class Hangman:
    def (, word):
        self.word =
        self.guessed = []

    def guess(, letter):
        print("You guessed the letter!")
        ###
        print("You guessed wrong!")
        ###
        print("You already guessed that letter")

    def get_status(self):
        print("Guess the word:")
        for  in self.word:
            if
                print(, end="")
            else:
                print("_", end="")
        print('\n')

    def check_if_player_won(self):


class :
    def (self):
        self.word =
        self.hanged =

    def (self):
        while :
            self.hanged.
            letter = input
            self.hanged.
            if self.hanged.:
                print("You won!")
                break


if  == "__main__":
