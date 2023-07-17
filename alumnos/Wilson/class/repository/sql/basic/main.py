import mysql.connector
from connector_database import ConnectorDatabase


class Repository:
    def __init__(self, connector):
        self.connector = connector

    def get_users(self):
        return self.connector.execute_query("SELECT * FROM alumnos")

    def get_user(self, id):
        return self.connector.execute_query("SELECT * FROM alumnos WHERE id = %s" % id)

    # TODO: Implement create user

    # TODO: Implement update user

    # TODO: Implement delete user


if __name__ == '__main__':
    # TODO: Create a connector object

    # TODO: Create a repository object

    # TODO: Get all users

    # TODO: Get user by id

    # TODO: Create a new user


