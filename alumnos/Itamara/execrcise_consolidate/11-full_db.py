# Genera un script que pueda crear una base de datos de estudiantes
# con una tabla llamada estudiantes que tenga dos campos.
# Inserta un registro en la tabla estudiantes con dos campos.
# Consulta todos los registros de la tabla estudiantes y muéstralos en pantalla.
# Consulta un registro de la tabla estudiantes y muéstralo en pantalla.
# Cada ejecución del script tiene que estar en funciones separadas

import mysql.connector
def connection_database(host, user, password, database):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        port=int(3307),
        database="alumnos"
    )
    return connection

def insert_data(row):
    insert=row.connect("INSERT INTO coches (id, modelo, marca) VALUES (1, 'Yaris', 'Toyota');")
    execute_query(conn, insert)


def get_data(show_table):
    get_all=show_table.connect("SELECT * FROM coches;")
    execute_query(conn, get_all)


def get_data_by_id(show_id_row):
    get_id=show_id_row.connector("SELECT id FROM coches;")
    execute_query(conn, get_id)

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


 if __name__ == '__main__':
     host = 'localhost',
     user = 'root',
     password = 'root',
     port = int(3307),
     database = "mysql"

     connection_database(host, user, password, database)
     conn = connection_database()

