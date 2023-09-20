import random


class ChoiceWord:
    def __init__(self):
        self.words = ["pepe", "casa", "padre", "marido", "mujer", "hombre"]

    def get_word(self):
        return random.choice(self.words)


class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed = []

    def guess(self, letter):
        if letter in self.word and letter not in self.guessed:
            self.guessed.append(letter)
            print("You guessed the letter!")
        elif letter not in self.word and letter not in self.guessed:
            self.guessed.append(letter)
            print("You guessed wrong!")
        else:
            print("You already guessed that letter")

    def get_status(self):
        print("Guess the word:")
        for letter in self.word:
            if letter in self.guessed:
                # Se agregar el argumento end="" para que no se haga un salto de linea
                print(letter, end="")
            else:
                print("_", end="")
        print('\n')

    def check_if_player_won(self):
        return set(self.word) == set(self.guessed)


class PlayGame:
    def __init__(self):
        self.word = ChoiceWord().get_word()
        self.hanged = Hangman(self.word)

    def play(self):
        while True:
            self.hanged.get_status()
            letter = input("Guess the letter: ")
            self.hanged.guess(letter)
            if self.hanged.check_if_player_won():
                print("You won!")
                break


if __name__ == "__main__":
    PlayGame().play()
