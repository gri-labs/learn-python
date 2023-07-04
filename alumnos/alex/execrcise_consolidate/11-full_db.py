# Genera un script que pueda crear una base de datos de estudiantes
# con una tabla llamada estudiantes que tenga dos campos.
# Inserta un registro en la tabla estudiantes con dos campos.
# Consulta todos los registros de la tabla estudiantes y muéstralos en pantalla.
# Consulta un registro de la tabla estudiantes y muéstralo en pantalla.
# Cada ejecución del script tiene que estar en funciones separadas
import mysql.connector


def connection_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mysql",
        port=int(3307),
    )

    return connection


def create_database(connect):
    query = "CREATE DATABASE IF NOT EXISTS estudiantes;"
    commit_query(connect, query)


def create_table(connect):
    query = "CREATE TABLE IF NOT EXISTS `estudiantes`.`estudiantes`(id INT, nombre VARCHAR(50), carrera VARCHAR(50));"
    commit_query(connect, query)


def insert_data(connect):
    query = "INSERT INTO `estudiantes`.`estudiantes` (nombre, carrera) VALUES ('Alex', 'Matemáticas')"
    commit_query(connect, query)


def get_data(connect):
    query = "SELECT * FROM `estudiantes`.`estudiantes`;"
    connect.cursor.execute(query)



def commit_query(connect, query):
    cursor = connect.cursor()
    cursor.execute(query)
    connect.commit()
    cursor.close()

def print_data(connect):
    get_data(connect)
    rows = connect.cursor.fetchall()
    for row in rows:
        print(row)
    connect.cursor.close()
    connect.close()


def close_connection(connection):
    connection.close()


if __name__ == '__main__':
    conn = connection_database()
    create_database(conn)
    create_table(conn)
    insert_data(conn)
    print_data(conn)

    