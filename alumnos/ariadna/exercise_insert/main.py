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


def execute_query_select(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


def insert_data(connection):
    for i in range(10):
        nombre = "Maria%s" % i
        query = "INSERT INTO estudiantes (`nombre`) VALUES ('%s');" % nombre
        commit_query(connection, query)
        print("Se insertó el registro %s" % i)


def delete_data(connection):
    query = "DELETE FROM estudiantes;"
    commit_query(connection, query)


def get_data_by_id(connection, student_id):
    query = "SELECT * FROM estudiantes WHERE id = %s;" % student_id
    result = execute_query_select(connection, query)
    return result


def select_action(action):
    if action == "INSERT":
        insert_data(conn)
    elif action == "GET_BY_ID":
        student_id = input("id: ")
        print(get_data_by_id(conn, student_id))
    elif action == "DELETE":
        delete_data(conn)


if __name__ == '__main__':
    conn = connection_database("localhost", "root", "root", "estudiantes", 3307)

    action = input("Ingrese la accion  ")
    select_action(action)