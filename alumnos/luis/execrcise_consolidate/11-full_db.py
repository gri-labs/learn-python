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


def create_database(connection):
    cursor = connection.cursor()
    create_database_sql = "CREATE DATABASE IF NOT EXISTS estudiantes;"
    cursor.execute(create_database_sql)
    connection.commit()


def create_table(connection):
    cursor = connection.cursor()
    create_table_sql = "CREATE TABLE IF NOT EXISTS `estudiantes`.`estudiantes`( id INT, nombre VARCHAR(255));"
    cursor.execute(create_table_sql)
    connection.commit()


def insert_data(connection):
    cursor = connection.cursor()
    insert_sql = "INSERT INTO estudiantes (nombre, carrera) VALUES ('luis', 'estudiante')"
    cursor.execute(insert_sql)
    connection.commit()


def get_data(connection):
    cursor = connection.cursor()
    select_sql = "SELECT * FROM mysql"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()
    return rows


def get_data_byid(connection):
    cursor = connection.cursor()
    select_sql = "SELECT carrera FROM mysql WHERE nombre=luis"
    cursor.execute(select_sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()
    return rows


def close_connection(connection):
    connection.close()


def run(connection):
    create_database(connection)
    create_table(connection)
    insert_data(connection)
    get_data(connection)
    close_connection(connection)


if __name__ == '__main__':
    conn = connection_database('localhost', 'root', 'root', 'mysql', 3308)
    run(conn)
