import mysql.connector
from generate_data import GenerateData

data = GenerateData()


def connection_database(host, user, password, database, port):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(port),
    )

    return connection


def execute_query_with_commit(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def populate_database(connection):
    for i in range(1000000):
        query = "INSERT INTO estudiantes (nombre) VALUES ('%s');" % data.get_name()
        try:
            execute_query_with_commit(connection, query)
            print(query)
        except Exception as e:
            print("Error: %s" % e)
        print("Se inserto el registro %s" % i)


def delete_database(connection):
    query = "DELETE FROM estudiantes;"
    execute_query_with_commit(connection, query)


def selector_type_of_query(type_query, connection):
    if type_query.lower() == 'insert':
        populate_database(connection)
    elif type_query.lower() == 'delete':
        delete_database(connection)
    else:
        print('No existe esa instruccion')


if __name__ == '__main__':
    connection = connection_database('localhost', 'root', 'root', 'gri', '3308')
    type_instruction = input('Ingrese el tipo de instruccion: ')
    selector_type_of_query(type_instruction, connection)
    connection.close()
