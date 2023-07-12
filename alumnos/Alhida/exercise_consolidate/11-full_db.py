# Genera un script que pueda crear una base de datos de estudiantes
# con una tabla llamada estudiantes que tenga dos campos.
# Inserta un registro en la tabla estudiantes con dos campos.
# Consulta todos los registros de la tabla estudiantes y muéstralos en pantalla.
# Consulta un registro de la tabla estudiantes y muéstralo en pantalla.
# Cada ejecución del script tiene que estar en funciones separadas

def connection_database():
    connection = mysql.connector.connect(
        host=localhost,
        user=root,
        password=root,
        database=estudiantes,
        port=int(3707),
    )

    return connection


def create_database(connect):
    query = "CREATE DATABASE IF NOT EXISTS estudiantes;"
    commit_query(connect, query)


def create_table(connect):
    query = "CREATE TABLE IF NOT EXISTS `estudiantes`.`estudiantes` (id INT, nombre VARCHAR(255), email VARCHAR(255));"
    commit_query(connect, query)


def insert_data(connect):
    query = "INSERT INTO estudiantes(id, nombre, gmail)VALUES (2, 'mariana', 'mariana24@gmail.com')"
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
    cursor = connection.cursor()
    cursor.execute(query)
    rows_result = cursor.fetchall()
    cursor.close()
    return rows_result




def print_data(rows):
    for row in rows:
        print(row)


def close_connection(connection):
    connection.close()


if __name__ == '__main__':
    conn = connection_database()
    create_database(conn)
    create_table(conn)
    insert_data(conn)
    data = get_data(conn)
    print_data(data)
    close_connection(conn)