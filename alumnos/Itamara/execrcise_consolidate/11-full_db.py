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
    execute_query_and_commit(connect, query)


def create_table(connect):
    query = "CREATE TABLE IF NOT EXISTS `gri`.`estudiantes` (id INT, nombre VARCHAR(50));"
    execute_query_and_commit(connect, query)


def insert_data(connect):
    query = "INSERT INTO `gri`.`estudiantes` (id, nombre) VALUES (1, 'Maria');"
    execute_query_and_commit(connect, query)


def get_data(connect):
    query = "SELECT * FROM `gri`.`estudiantes`;"
    return execute_query(connect, query)


def delete_data(connect):
    query = "DELETE FROM `gri`.`estudiantes` WHERE nombre = 'Maria';"
    execute_query_and_commit(connect, query)

def execute_query_and_commit(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


def show_data(data):
    for row in data:
        print(row)


def close_connection(connection):
    connection.close()


def run(connection):
    create_database(connection)
    create_table(connection)
    insert_data(connection)
    data = get_data(connection)
    show_data(data)
    delete_data(connection)
    data = get_data(connection)
    show_data(data)
    close_connection(connection)


if __name__ == '__main__':
    conn = connection_database('localhost', 'root', 'root', 'gri', 3307)
    run(conn)