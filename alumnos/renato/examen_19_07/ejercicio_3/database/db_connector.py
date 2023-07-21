import mysql.connector


class DBConnector:
    def __init__(self):
        pass

    def connection_database(self, host, user, password, port, database_name):
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=int(port),
            database=database_name,
        )
        return connection

    def create_db(self, connection, db_name):
        sql_code = f"""
        CREATE DATABASE IF NOT EXISTS {db_name};
        """
        self.exec_and_commit(connection, sql_code)

    def create_table(self, connection, db_name, table_name):
        sql_code = f"""
        CREATE TABLE IF NOT EXISTS {db_name}.{table_name} (
        id INT,
        name VARCHAR(25),
        age INT
        );
        """
        self.exec_and_commit(connection, sql_code)

    def execute_query_select(self, connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def exec_and_commit(self, connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()

    def close_connection(self, connection):
        connection.close()
