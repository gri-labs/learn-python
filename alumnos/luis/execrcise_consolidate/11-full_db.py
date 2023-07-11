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
    sql = "CREATE DATABASE IF NOT EXISTS estudiantes;"
    exec_sql_commit(connect, sql)


def use_database(connect):
    sql = "USE `estudiantes`;"
    exec_sql_commit(connect, sql)


def create_table(connect):
    sql = "CREATE TABLE IF NOT EXISTS `estudiantes`.`estudiantes`(id INT, nombre VARCHAR(255));"
    exec_sql_commit(connect, sql)


def insert_data(connect):
    sql = "INSERT INTO `estudiantes`.`estudiantes` (id, nombre) VALUES (1, 'luis');"
    exec_sql_commit(connect, sql)


def get_data(connect):
    sql = "SELECT * FROM `estudiantes`.`estudiantes`;"
    return exec_sql(connect, sql)


def get_data_byid(connect):
    sql = "SELECT id FROM estudiantes WHERE nombre ='luis';"
    return exec_sql(connect, sql)


def delete_data(connect):
    sql = "DELETE FROM `estudiantes`.`estudiantes` WHERE nombre = 'luis';"
    exec_sql_commit(connect, sql)


def mostrardatos(data):
    for row in data:
        print(row)


def exec_sql(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    return data


def exec_sql_commit(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    cursor.close()


def close_connection(connection):
    connection.close()


def run(connection):
    create_database(connection)
    use_database(connection)
    create_table(connection)
    insert_data(connection)
    get_data(connection)
    get_data_byid(connection)
    data = get_data(connection)
    mostrardatos(data)
    delete_data(connection)
    close_connection(connection)


if __name__ == '__main__':
    conn = connection_database('localhost', 'root', 'root', 'estudiantes', 3307)
    run(conn)