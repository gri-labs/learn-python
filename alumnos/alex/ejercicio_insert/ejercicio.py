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
def insert_datos(connection):
    i = 0
    while i < 10000:
        query = "INSERT INTO estudiantes (`nombre`) VALUES ('Pepe%s');" % (i)
        execute_query_and_commit(connection, query)
        i = i + 1
    connection.cursor.close()
if __name__ == '__main__':
    x = input()
    if x == "INSERT":
        insert_datos(connection_database())
