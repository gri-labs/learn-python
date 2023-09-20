import unittest
from games.rock_paper_scissors.main import Computer
from games.rock_paper_scissors.main import Game
from games.rock_paper_scissors.main import Player


class TestRockPaperScissors(unittest.TestCase):

    # Método es un método de unittest que se ejecuta antes de cada prueba
    # Para crear las instancias necesarias para las pruebas
    def setUp(self):
        self.player = Player()
        self.computer = Computer()
        self.game = Game(self.player, self.computer)

    def test_compare_draw(self):
        player_option = 'rock'
        computer_option = 'rock'

        self.game.compare(player_option, computer_option)
        self.assertEqual(self.player.score, 0)
        self.assertEqual(self.computer.score, 0)


if __name__ == '__main__':
    unittest.main()
