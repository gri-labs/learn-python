# Genera un script que pueda crear una base de datos de estudiantes
# con una tabla llamada estudiantes que tenga dos campos.
# Inserta un registro en la tabla estudiantes con dos campos.
# Consulta todos los registros de la tabla estudiantes y muéstralos en pantalla.
# Consulta un registro de la tabla estudiantes y muéstralo en pantalla.
# Cada ejecución del script tiene que estar en funciones separadas

import logging
import mysql.connector


def connection_database(host, user, password, port, database_name):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=int(port),
        database=database_name,
    )
    return connection


def create_db(connection, db_name):
    sql_code = f"""
    CREATE DATABASE IF NOT EXISTS {db_name};
    """
    exec_and_commit(connection, sql_code)


def create_table(connection, db_name, table_name):
    sql_code = f"""
    CREATE TABLE IF NOT EXISTS {db_name}.{table_name} (
    id INT,
    nombre VARCHAR(25),
    carrera VARCHAR(255)
    );
    """
    exec_and_commit(connection, sql_code)


def insert_data(connection, db_name, table_name, row_id, name, career):
    sql_code = f"""
    INSERT INTO {db_name}.{table_name} (id, nombre, carrera)
    VALUES ('{row_id}', '{name}', '{career}')
    """
    exec_and_commit(connection, sql_code)
    return


def get_data(connection, db_name, table_name):
    sql_code = f"""
    SELECT * FROM {db_name}.{table_name}
    """
    results = execute_query_select(connection, sql_code)
    return results


def get_data_by_id(connection, db_name, table_name, id):
    sql_code = f"""
    SELECT * FROM {db_name}.{table_name} WHERE id = {id}
    """
    results = execute_query_select(connection, sql_code)
    return results


def execute_query_select(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def print_data(to_print):
    for result in to_print:
        print(result)


def exec_and_commit(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def close_connection(connection):
    connection.close()


# Arranque del servidor o inicio del programa
if __name__ == '__main__':
    # Se configura el log
    logging.basicConfig(filename='request.log', level=logging.DEBUG)

    # Creo DB MyNewDb in MySQL
    connection_db = connection_database('localhost', 'root', 'root', 3307, 'mysql')
    create_db(connection_db, "myNewDb")

    # Creo Tabla
    create_table(connection_db, "myNewDb", "NewEstudiantes")

    # Añado un usuario
    insert_data(connection_db, "myNewDb", "NewEstudiantes", 2, "Merlin", "Gato")

    # Enseño todos
    all_data = get_data(connection_db, "myNewDb", "NewEstudiantes")

    # Enseño uno
    data_by_id = get_data_by_id(connection_db, "myNewDb", "NewEstudiantes", 1)

    print_data(all_data)
    print_data(data_by_id)

    close_connection(connection_db)
