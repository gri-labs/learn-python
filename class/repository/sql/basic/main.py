import mysql.connector
from connector_database import ConnectorDatabase


class Repository:
    def __init__(self, connector):
        self.connector = connector

    def get_users(self):
        return self.connector.execute_query("SELECT * FROM alumnos")

    # TODO: Implement get user by id

    # TODO: Implement create user

    # TODO: Implement update user

    # TODO: Implement delete user


if __name__ == '__main__':
    # TODO: Instancia el repositorio con el conector

    # TODO: Get all users

    # TODO: Implementa una clase para printar datos
    # TODO: Print users

    # TODO: Get user by id

    # TODO: Create a new user


