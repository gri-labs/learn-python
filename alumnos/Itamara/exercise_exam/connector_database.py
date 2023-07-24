import mysql.connector


class ConnectorDatabase:

    def __init__(self, host, user, password, database, port):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="gri",
            port=int(3307)
        )

    def execute_and_fetchall(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def execute_and_fetchone(self, query):

    def execute_and_commit(self, query):

    def close_connection(self):
        self.connection.close()
