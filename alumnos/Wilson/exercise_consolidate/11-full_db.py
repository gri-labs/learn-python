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
    cursor = connection.cursor()
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
    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()


def insert_data(connection):
    # Crear el objeto cursor para ejecutar sentencias SQL
    cursor = connection.cursor()

    # Insertar un registro
    insert_sql = "INSERT INTO estudiantes (id, nombre) VALUES (1, 'Wilson');"

    # Ejecutar los cambios en la base de datos
    cursor.execute(insert_sql)

    # Confirmar los cambios en la base de datos
    connection.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()


def get_data(connection):
    # Crear un cursor para ejecutar sentencias SQL
    cursor = connection.cursor()

    # Consultar todos los registros
    select_sql = "SELECT nombre FROM estudiantes"

    # Ejecutar los cambios en la base de datos
    cursor.execute(select_sql)

    # Obtener los resultados
    rows = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()
    return rows


def get_data_by_id(connection, id_number):
    # Crear un cursor para ejecutar sentencias SQL
    cursor = connection.cursor()

    # Consultar todos los registros
    select_sql = f"SELECT id FROM estudiantes WHERE id ={id_number}"

    # Ejecutar los cambios en la base de datos
    cursor.execute(select_sql)

    # Obtener los resultados
    rows = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()
    return rows


if __name__ == '__main__':
    conn = connection_database('127.0.0.1', 'root', 'root', 'estudiantes')
    create_table(conn)
    insert_data(conn)
    print(get_data(conn))
    print(get_data_by_id(conn, 1))
