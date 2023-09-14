from random import randint


class GenerateGuessNumber:

    def __init__(self):
        self.guess_numer = 0

    def generate(self):
        self.guess_numer = randint(1, 10)
        return self.guess_numer


class PlayGuessNumber:

    def __init__(self, generate_guess_number):
        self.generate_guess_number = generate_guess_number
        self.guess_number = 0

    def play(self):
        self.guess_number = int(input('Guess a number between 1 and 10: '))

    def is_correct(self):
        return self.guess_number == self.generate_guess_number.guess_numer

    def is_greater(self):
        return self.guess_number > self.generate_guess_number.guess_numer

    def is_lower(self):
        return self.guess_number < self.generate_guess_number.guess_numer


if __name__ == '__main__':
    generated_guess_number = GenerateGuessNumber()
    generated_guess_number.generate()

    play_guess_number = PlayGuessNumber(generated_guess_number)

    while True:
        play_guess_number.play()

        if play_guess_number.is_correct():
            print('You win')
            break
        elif play_guess_number.is_greater():
            print('Lower')
        elif play_guess_number.is_lower():
            print('Greater')
