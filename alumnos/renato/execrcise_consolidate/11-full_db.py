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
    return


def create_table(connection, db_name, table_name):
    sql_code = f"""
    CREATE TABLE IF NOT EXISTS {db_name}.{table_name} (
    id INT,
    nombre VARCHAR(25),
    carrera VARCHAR(255)
    );
    """
    exec_and_commit(connection, sql_code)
    return


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
    cursor = connection.cursor()
    exec_only(cursor, sql_code)
    results = cursor.fetchall()
    print_data(results)
    return


def get_data_by_id(connection, db_name, table_name, id):
    sql_code = f"""
    SELECT * FROM {db_name}.{table_name} WHERE id = {id}
    """
    cursor = connection.cursor()
    exec_only(cursor, sql_code)
    results = cursor.fetchone()
    print_data(results)
    return


def print_data(to_print):
    for result in to_print:
        print(result)
    return


def exec_and_commit(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def exec_only(cursor, query):
    cursor.execute(query)


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
    insert_data(connection_db, "myNewDb", "NewEstudiantes", 1, "Ginger", "Gato")

    # Enseño todos
    get_data(connection_db, "myNewDb", "NewEstudiantes")

    # Enseño uno
    get_data_by_id(connection_db, "myNewDb", "NewEstudiantes", 1)

    connection_db.close()
