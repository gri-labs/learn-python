# Genera un script que pueda crear una base de datos de estudiantes
# con una tabla llamada estudiantes que tenga dos campos.
# Inserta un registro en la tabla estudiantes con dos campos.
# Consulta todos los registros de la tabla estudiantes y muéstralos en pantalla.
# Consulta un registro de la tabla estudiantes y muéstralo en pantalla.
# Cada ejecución del script tiene que estar en funciones separadas
import mysql.connector


def connection_database(host,user,password,database,port):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(port),
    )
    return connection


def create_database(connection):
    query = "CREATE DATABASE IF NOT EXISTS estudiantes;"
    commit_query(connection, query)


def create_table(connection):
    query = "CREATE DATABASE IF NOT EXISTS `estudiantes`.`estudiantes` (id INT, nombre VARCHAR(255));"
    commit_query(connection, query)


def insert_data(connection):
    query = "INSERT INTO estudiantes (id, nombre) VALUES (1, 'Jesus');"
    commit_query(connection, query)


def get_data(connection):
    query = "SELECT * FROM `estudiantes`.`estudiantes`;"
    return execute_query_select(connection, query)


def delete_data(connection):
    query = "DELETE FROM `estudiantes`.`estudiantes` WHERE nombre = 'Jesus';"
    execute_query_select(connection, query)


def commit_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


# def get_data_by_id():


def execute_query_select(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result
    

def print_data(rows):
    for row in rows:
        print(row)


def close_connection(connection):
    connection.close()


def ejecutar_todo(connection):
    create_database(connection)
    create_table(connection)
    insert_data(connection)
    res = get_data(connection)
    print_data(res)
    delete_data(connection)
    res = get_data(connection)
    print_data(res)
    close_connection(connection)


if __name__ == '__main__':
    conn = connection_database('localhost', 'root', 'root', 'estudiantes', 3307)
    ejecutar_todo(conn)