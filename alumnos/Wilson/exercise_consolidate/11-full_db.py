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
        database=database,
        port=int(3308),
    )
    return connection


def create_table(connection):
    # creo el cursor
    cursor = connection.cursor()
    # crear la base de datos
    create_database_sql = "CREATE DATABASE IF NOT EXISTS estudiantes;"
    # Crear una tabla
    create_table_sql = "CREATE TABLE IF NOT EXISTS `estudiantes`.`estudiantes` (id INT, nombre VARCHAR(255));"

    # Ejecutar los cambios en la base de datos
    cursor.execute(create_database_sql)
    # Confirmar los cambios en la base de datos
    connection.commit()
    # Ejecutar los cambios en la base de datos
    cursor.execute(create_table_sql)
    # Confirmar los cambios en la base de datos
    connection.commit()
    return cursor


def insert_data(connection, cursor):
    # Insertar un registro
    insert_sql = "INSERT INTO estudiantes (id, nombre) VALUES (1, 'Wilson');"

    # Ejecutar los cambios en la base de datos
    cursor.execute(insert_sql)

    # Confirmar los cambios en la base de datos
    connection.commit()


def get_data(connection, cursor):
    # Consultar todos los registros
    select_sql = "SELECT nombre FROM estudiantes"

    # Ejecutar los cambios en la base de datos
    cursor.execute(select_sql)

    # Obtener los resultados
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    return rows


def get_data_by_id(connection, cursor, id_number):
    # Consultar todos los registros
    select_sql = f"SELECT id FROM estudiantes WHERE id ={id_number}"

    # Ejecutar los cambios en la base de datos
    cursor.execute(select_sql)

    # Obtener los resultados
    rows = cursor.fetchall()

    return rows


def delete_data_by_id(connection, cursor, id_number):
    # Consultar todos los registros
    select_sql = f"DELETE FROM estudiantes.estudiantes WHERE id ={id_number}"

    # Ejecutar los cambios en la base de datos
    cursor.execute(select_sql)

    # Obtener los resultados
    rows = cursor.fetchall()

    return rows


def close_all_connections(connection, cursor):
    connection.close()
    cursor.close()


if __name__ == '__main__':
    conn = connection_database('127.0.0.1', 'root', 'root', 'estudiantes')
    cursor = create_table(conn)
    insert_data(conn, cursor)
    get_data(conn, cursor)
    print(get_data_by_id(conn, cursor, 1))
    #delete_data_by_id(conn, cursor, 3)
    close_all_connections(conn, cursor)

