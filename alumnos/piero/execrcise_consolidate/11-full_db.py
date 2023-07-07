# Genera un script que pueda crear una base de datos de estudiantes
# con una tabla llamada estudiantes que tenga dos campos.
# Inserta un registro en la tabla estudiantes con dos campos.
# Consulta todos los registros de la tabla estudiantes y muéstralos en pantalla.
# Consulta un registro de la tabla estudiantes y muéstralo en pantalla.
# Cada ejecución del script tiene que estar en funciones separadas

import mysql.connector

def connection_database():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        port=int(3307),
        database='estudiantes'
)
    return connection

def create_database(connection):
    cursor = connection.cursor()
    create_database_sql = "CREATE DATABASE IF NOT EXISTS estudiantes"
    cursor.execute(create_database_sql)
    cursor.close

def create_table(connection):
    cursor = connection.cursor()
    create_table_sql = "CREATE TABLE IF NOT EXISTS estudiante (id INT NOT NULL,nombre VARCHAR(100),carrera VARCHAR(100))"
    cursor.execute(create_table_sql)
    cursor.close


def insert_data(connection):
    cursor = connection.cursor()
    insert_sql = "INSERT INTO estudiante (id, nombre, carrera) VALUES (1, 'Piero', 'Profe')"
    cursor.execute(insert_sql)
    connection.commit()
    cursor.close


def get_data(connection):
    cursor = connection.cursor()
    select_sql = "SELECT * FROM estudiante"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close

def get_data_by_id(connection):
    cursor = connection.cursor()
    select_sql = "SELECT * FROM estudiante WHERE id = 1"
    cursor.execute(select_sql)
    result = cursor.fetchone()
    print(result)
    cursor.close()


if __name__ == '__main__':
    conn = connection_database("localhost", "root", "root", "estudiantes")
    create_database(conn)
    create_table(conn)
    insert_data(conn)
    get_data(conn)
    get_data_by_id(conn)
    conn.close()