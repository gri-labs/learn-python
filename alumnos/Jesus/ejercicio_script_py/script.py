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


def commit_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def close_connection(connection):
    connection.close()


def insertar_datos(connection):
    i = 0
    while i < 10000:
        query = "insert into `estudiantes` (nombre) value ('Jesus%s')" % i
        i = i + 1
        commit_query(connection, query)
    close_connection(connection)


def borrar_datos(connection):
    query = "delete from estudiantes"
    commit_query(connection, query)
    close_connection(connection)


def ejecuta_opcion(query_option, connection):
    if query_option.lower() == 'insert':
        insertar_datos(connection)
        print('Datos insertados')
    elif query_option.lower() == 'delete':
        print('Datos borrados')


if __name__ == '__main__':
    connection = connection_database('localhost', 'root', 'root', 'estudiantes', 3307)
    orden = input('Ingrese la instruccion insert o delete: ')
    ejecuta_opcion(orden, connection)
