import mysql.connector


class RepositoryDB:
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

    def insert_data(self, connection, db_name, table_name, row_id, name, age):
        sql_code = f"""
        INSERT INTO {db_name}.{table_name} (id, name, age)
        VALUES ('{row_id}', '{name}', '{age}')
        """
        self.exec_and_commit(connection, sql_code)
        return

    def get_data_by_id(self, connection, db_name, table_name, id):
        sql_code = f"""
        SELECT * FROM {db_name}.{table_name} WHERE id = {id}
        """
        results = self.execute_query_select(connection, sql_code)
        return results

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
