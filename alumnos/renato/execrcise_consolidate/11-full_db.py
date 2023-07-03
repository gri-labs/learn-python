# Genera un script que pueda crear una base de datos de estudiantes
# con una tabla llamada estudiantes que tenga dos campos.
# Inserta un registro en la tabla estudiantes con dos campos.
# Consulta todos los registros de la tabla estudiantes y muéstralos en pantalla.
# Consulta un registro de la tabla estudiantes y muéstralo en pantalla.
# Cada ejecución del script tiene que estar en funciones separadas

import logging
import mysql.connector


def connection_database(database_name):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        port=int(3307),
        database=database_name,
    )
    connection.connect()
    return connection


def create_db(db_name):
    create_database_sql = f"""
    CREATE DATABASE IF NOT EXISTS {db_name};
    """
    return create_database_sql


def create_table(db_name, table_name):
    create_tbl_sql = f"""
    CREATE TABLE IF NOT EXISTS {db_name}.{table_name} (
    id INT,
    nombre VARCHAR(25),
    carrera VARCHAR(255)
    );
    """
    return create_tbl_sql


def insert_data(tabla, id, name, career):
    insert_sql = f"""
    INSERT INTO {tabla} (id, nombre, carrera)
    VALUES ('{id}', '{name}', '{career}')
    """
    return insert_sql


def get_data(name_db):
    select_sql = f"""
    SELECT * FROM {name_db}
    """
    return select_sql


def get_data_by_id(name_db, id):
    select_sql = f"""
    SELECT * FROM {name_db} WHERE id = {id}
    """
    return select_sql


def exec_and_commit(cursor, connection, query):
    cursor.execute(query)
    connection.commit()


def exec(cursor, query):
    cursor.execute(query)


# Arranque del servidor o inicio del programa
if __name__ == '__main__':
    # Se configura el log
    logging.basicConfig(filename='request.log', level=logging.DEBUG)

    # Creo DB MyNewDb in MySQL
    connection_db = connection_database('mysql')
    cursor_db = connection_db.cursor()
    create_db_sql = create_db("MyNewDb")
    exec_and_commit(cursor_db, connection_db, create_db_sql)

    # Creo Tabla
    create_table_sql = create_table("MyNewDb", "NewEstudiantes")
    exec_and_commit(cursor_db, connection_db, create_table_sql)
    cursor_db.close()
    connection_db.close()

    # Añado un usuario
    connection_db = connection_database('MyNewDb')
    cursor_db = connection_db.cursor()
    insert_data_sql = insert_data("NewEstudiantes", 1, "Ginger", "Gato")
    exec_and_commit(cursor_db, connection_db, insert_data_sql)

    # Enseño todos
    get_all_sql = get_data("NewEstudiantes")
    exec(cursor_db, get_all_sql)
    rows = cursor_db.fetchall()
    for row in rows:
        print(row)

    # Enseño uno
    get_by_id_sql = get_data_by_id("NewEstudiantes", 1)
    exec(cursor_db, get_by_id_sql)
    rows = cursor_db.fetchone()
    for row in rows:
        print(row)

    cursor_db.close()
    connection_db.close()

