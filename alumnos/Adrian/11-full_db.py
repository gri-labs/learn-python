# Genera un script que pueda crear una base de datos de estudiantes
# con una tabla llamada estudiantes que tenga dos campos.
# Inserta un registro en la tabla estudiantes con dos campos.
# Consulta todos los registros de la tabla estudiantes y muéstralos en pantalla.
# Consulta un registro de la tabla estudiantes y muéstralo en pantalla.
# Cada ejecución del script tiene que estar en funciones separadas
import mysql.connector


def connection_database():
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(port),
    )

    return connection


def create_database(connect):
    query = "CREATE DATABASE IF NOT EXISTS gri;"
    commit_query(connect, query)


def create_table(connect):
    query = "CREATE TABLE IF NOT EXISTS 'gri'.'ESTUDIANTES'(id INT, nombre VARCHAR(255), edad INT)"
    commit_query(connect, query)


def insert_data(connect):
    query = "INSERT INTO estudiantes (nombre, edad) VALUES ('Pepe',33);"
    commit_query(connect, query)


def get_data(connect):
    query = "SELECT * FROM `gri`.`estudiantes`;"
    return execute_query_select(connect, query)

def get_single_data(connect):
    query = "SELECT * FROM estudiantes WHERE id = 1;"
    return execute_query_select(connect, query)


def commit_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def execute_query_select(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


def print_data(rows):
    for row in rows:
        print(row)


def close_connection(connection):
    connection.close()


if __name__ == '__main__':
    conn = connection_database('localhost','root','root','gri',3308)
    create_database(conn)
    create_table(conn)
    insert_data(conn)
    data = get_data(conn)
    print_data(data)
    single_data = get_single_data(conn)
    print_data(single_data)
    close_connection(conn)
