import mysql.connector


class ConnectorDatabaseBasic:

    def __init__(self, host, user, password, database, port):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=int(port)
        )

    def execute_and_fetchall(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def execute_and_fetchone(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result
