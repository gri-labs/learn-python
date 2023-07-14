import mysql.connector


def connection_database():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='estudiantes',
        port=int(3307),
        )
    return connection

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

def insert_datos(connection):
    i = 0
    while i < 10000:
        query = "INSERT INTO estudiantes (`nombre`) VALUES ('Pepe%s');" % (i)
        execute_query_and_commit(connection, query)
        i = i + 1

def quering_id(connection, num):
    query = "SELECT * FROM estudiantes WHERE id = %s;" % num
    result = execute_query(connection, query)
    return result

def switch_inicial():
    modalidad = input("Qué quieres hacer: SELECT/INSERT? ")
    if modalidad == "INSERT":
        insert_datos(connection_database())
    if modalidad == "SELECT":
        estudiante_id = input("id: ")
        print(quering_id(connection_database(), estudiante_id))

if __name__ == '__main__':
    switch_inicial()





