import random


class Computer:
    def __init__(self):
        self.name = 'Computer'
        self.score = 0

    def add_score(self):
        self.score = self.score + 1

    def get_option(self):
        return random.choice(['rock', 'paper', 'scissors'])


class Player:
    def __init__(self):
        self.name = ''
        self.score = 0

    def add_score(self):
        self.score = self.score + 1


class Game:

    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def compare(self, player_option, computer_option):

        if player_option == computer_option:
            print('Draw')
        elif (
                player_option == 'rock' and computer_option == 'scissors' or
                player_option == 'paper' and computer_option == 'rock' or
                player_option == 'scissors' and computer_option == 'paper'
        ):
            self.player.add_score()
            print("Win! Added new point, congratulations, your raiting is: ", self.player.score)
        else:
            self.computer.add_score()
            print("Lose! added point to computer, the computer raiting is: ", self.computer.score)


class Play:
    def __init__(self, game):
        self.game = game

    def play(self):
        self.game.player.name = input('Enter your name: ')
        print("Okay, let's start")
        while True:
            self.show_options()
            player_option = input("Enter your choice:")
            computer_option = self.game.computer.get_option()
            self.game.compare(player_option, computer_option)
            self.check_win()

    def check_win(self):
        if self.game.player.score == 3:
            print("You win the game")
            exit()
        elif self.game.computer.score == 3:
            print("You lose the game")
            exit()

    def show_options(self):
        print("Available options:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")


if __name__ == '__main__':
    Play(Game(Player(), Computer())).play()
