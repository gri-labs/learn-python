# Genera un script que pueda crear una base de datos de estudiantes
# con una tabla llamada estudiantes que tenga dos campos.
# Inserta un registro en la tabla estudiantes con dos campos.
# Consulta todos los registros de la tabla estudiantes y muéstralos en pantalla.
# Consulta un registro de la tabla estudiantes y muéstralo en pantalla.
# Cada ejecución del script tiene que estar en funciones separadas
import mysql.connector


def connection_database(host, user, password, database, port):
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
    query = "CREATE TABLE IF NOT EXISTS `gri`.`estudiantes` (id INT, nombre VARCHAR(255));"
    commit_query(connect, query)


def insert_data(connect):
    query = ""
    commit_query(connect, query)


def get_data(connect):
    query = "SELECT * FROM `gri`.`estudiantes`;"
    return execute_query_select(connect, query)


def commit_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def execute_query_select(connection, query):


def print_data(rows):
    for row in rows:
        print(row)


def close_connection(connection):
    connection.close()

def run(connection):
    create_database(connection)
    create_table(connection)
    insert_data()
    data = get_data()
    print_data()
    close_connection()


if __name__ == '__main__':
    conn = connection_database('localhost', 'root', 'root', 'mysql', 3308)
    run(conn)

