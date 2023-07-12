# Genera un script que pueda crear una base de datos de estudiantes
# con una tabla llamada estudiantes que tenga dos campos.
# Inserta un registro en la tabla estudiantes con dos campos.
# Consulta todos los registros de la tabla estudiantes y muéstralos en pantalla.
# Consulta un registro de la tabla estudiantes y muéstralo en pantalla.
# Cada ejecución del script tiene que estar en funciones separadas

import mysql.connector

def connection_database(host, user, password, database):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=int(3307),
        database=database
)
    return connection

def cursor_commit_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()

def execute_query(query, connection):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def create_database(connection):
    cursor_commit_query(connection, "CREATE DATABASE IF NOT EXISTS estudiantes")

def create_table(connection):
    cursor_commit_query(connection, "CREATE TABLE IF NOT EXISTS estudiante (id INT NOT NULL,nombre VARCHAR(100),carrera VARCHAR(100))")

def insert_data(connection):
    cursor_commit_query(connection, "INSERT INTO estudiante (id, nombre, carrera) VALUES (3, 'Thor', 'HijoDeOdin')")

def get_data(connection):
    rows = execute_query("SELECT * FROM estudiante", connection)
    for row in rows:
        print(row)

def get_data_by_id(connection):
    row = execute_query("SELECT * FROM estudiante WHERE id = 1", connection)
    print(row)

if __name__ == '__main__':
    conn = connection_database("localhost", "root", "root", "estudiantes")
    create_database(conn)
    create_table(conn)
    insert_data(conn)
    get_data(conn)
    get_data_by_id(conn)
    conn.close()