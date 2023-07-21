import mysql.connector


class ConnectorDatabase:

    def __init__(self, host, user, password, database, port):
        self.connection = mysql.connector.connect(
            host=,
            user=,
            password=,
            database=,
            port=int()
        )

    def execute_and_fetchall(self, query):


    def execute_and_fetchone(self, query):


    def execute_and_commit(self, query):


    def close_connection(self):
