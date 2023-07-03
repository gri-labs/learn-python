# Genera un script que pueda crear una base de datos de estudiantes
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port=int(3307),
    database=estudiantes
)
# con una tabla llamada estudiantes que tenga dos campos.
# Inserta un registro en la tabla estudiantes con dos campos.
# Consulta todos los registros de la tabla estudiantes y muéstralos en pantalla.
# Consulta un registro de la tabla estudiantes y muéstralo en pantalla.
# Cada ejecución del script tiene que estar en funciones separadas

def connection_database():
    create_database_sql = "CREATE DATABASE IF NOT EXISTS estudiantes;"
def create_table():
    create_table_sql = "CREATE TABLE IF NOT EXISTS `estudiantes`.`estudiantes`( id INT, nombre VARCHAR(255));"

def insert_data():
    insert_sql = """
    INSERT INTO estudiantes (nombre, carrera)
    VALUES ('luis', 'estudiante')
    """
def get_data():

def get_data_by_id():


if __name__ == '__main__':
