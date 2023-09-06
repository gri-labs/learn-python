import mysql.


class ConnectorDatabase:

    def __init__(self, ):
        self.connection = mysql.connector.connect(

        )

    def execute_and_commit(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
        except Exception as e:
            print(e)
            self.connection.rollback()
