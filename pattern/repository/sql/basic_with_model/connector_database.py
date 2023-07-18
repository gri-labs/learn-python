import mysql.connector


class ConnectorDatabase:

    def __init__(self, host, user, password, database, port):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=int(port)
        )

    def query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def transaction(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
        except Exception as e:
            print(e)
            self.connection.rollback()

    def close_connection(self):
        self.connection.close()
