import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=int(3307),
    database="estudiantes"
)

def execute_query_and_commit(connection, query):
    connection.cursor.execute(query)
    connection.commit()
def Insert(connection):
    i = 0
    while i < 10000:
        query = "INSERT INTO estudiantes (`id`, `nombre`) VALUES (null, 'Pepe%s');" % (i)
        execute_query_and_commit(connection, query)
    connection.cursor.close()
if __name__ == '__main__':
    x = input()
    if x == "INSERT":
        Insert(connection)
