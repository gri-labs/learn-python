from database import ConnectorDatabase


# InitGame es una clase que se encarga de obtener las preguntas de la base de datos
class InitGame:
    def __init__(self, connector_database):
        self.connector_database = connector_database

    def get_questions(self):
        query = "SELECT * FROM questions"
        return self.connector_database.get_all(query)


# Player es una clase que representa a un jugador
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


# TurnPlayer es una clase que hereda de la clase Player y representa a un jugador que juega un turno
# del juego
class TurnPlayer(Player):
    # El constructor de la clase recibe un nombre y llama al constructor de la clase base Player
    def __init__(self, name):
        # Llamada al constructor de la clase base Player
        super().__init__(name)
        self.action = None

    # El método turn recibe una pregunta y devuelve True si el jugador acierta la pregunta y False si falla
    def turn(self, question):
        self.action = input("Answer for %s: " % self.name)
        return self.action == question[2]


class Trivial:
    def __init__(self, questions, players, connector_database):
        self.questions = questions
        self.players = players
        self.connector_database = connector_database

    def choose(self):
        for question in self.questions:
            question_to_player = question[1]

            for player in self.players:
                print("Turn player: %s" % player.name)
                print(question_to_player)

                if player.turn(question):
                    player.score += 1
                    print("The answer of player %s is correct!" % player.name)
                else:
                    print("The answer of player %s, fail!" % player.name)

        self.show_score()
        self.save_score()

    def show_score(self):
        for player in self.players:
            print("The score of player %s is %d" % (player.name, player.score))

    def save_score(self):
        for player in self.players:
            query = f"INSERT INTO score (name, points) VALUES ('{player.name}', {player.score})"
            self.connector_database.execute_and_commit(query)


if __name__ == '__main__':
    connection = ConnectorDatabase(
        host='localhost',
        user='root',
        password='root',
        database='trivial',
        port=3308
    )
    number_of_players = int(input("How many players are going to play? "))
    player_names = [input(f"Name of player: {i + 1}: ") for i in range(number_of_players)]
    init_game = InitGame(connection)
    players = [TurnPlayer(name) for name in player_names]
    Trivial(init_game.get_questions(), players, connection).choose()
