from db_connector import DBConnector


class RepositoryDB:
    def __init__(self):
        pass

    def insert_data(self, connection, db_name, table_name, row_id, name, age):
        db_conn = DBConnector()
        sql_code = f"""
        INSERT INTO {db_name}.{table_name} (id, name, age)
        VALUES ('{row_id}', '{name}', '{age}')
        """
        db_conn.exec_and_commit(connection, sql_code)
        return

    def get_data_by_id(self, connection, db_name, table_name, id):
        db_conn = DBConnector()
        sql_code = f"""
        SELECT * FROM {db_name}.{table_name} WHERE id = {id}
        """
        results = db_conn.execute_query_select(connection, sql_code)
        return results
