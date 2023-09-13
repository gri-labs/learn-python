import mysql.connector


class ConnectorDatabase:

    def __init__(, ):
        .connection = .connect(
            host=,
            user=,
            password=,
            database=,
            port=int()
        )

    def execute_and_fetchone(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.
        cursor.close()
        return result

    def execute_and_commit(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
        except Exception as e:
            print(e)
            self.connection.rollback()
