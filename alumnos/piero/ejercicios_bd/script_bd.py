import random
from faker import Faker
import mysql.connector

fake = Faker(['it_IT', 'es_ES', 'en_US'])


def connection_database(host, user, password, database):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=int(3307),
        database=database
    )
    return connection


def cursor_commit_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def execute_query(query, connection):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


def gen_correo_electronico(nombre, apellido):
    proveedor = fake.free_email_domain()
    correo_electronico = f"{nombre}.{apellido}@{proveedor}"
    return correo_electronico


def gen_nombre():
    nombre = fake.first_name()
    return nombre


def gen_apellido():
    apellido = fake.last_name()
    return apellido


def gen_edad():
    edad = random.randint(18, 65)
    return edad


def insert_data(connection):
    for i in range(1, 100000):
        correo_electronico = gen_correo_electronico(gen_nombre(), gen_apellido())
        nombre = gen_nombre()
        apellido = gen_apellido()
        edad = gen_edad()
        cursor_commit_query(connection, f"INSERT INTO usuarios (email, nombre, apellido, edad) VALUES ('{correo_electronico}', '{nombre}', '{apellido}', {edad})")


def delete_data(connection):
    cursor_commit_query(connection, "DELETE FROM usuarios")


def get_data(connection):
    rows = execute_query("SELECT * FROM usuarios", connection)
    if len(rows) == 0:
        print("No hay registros")
    else:
        for row in rows:
            print(row)


def get_data_by_id(connection):
    id= int(input(" indica que id quieres buscar:"))
    row = execute_query(f"SELECT * FROM usuarios WHERE id = {id}", connection)
    if len(row) == 0:
        print("ID no encontrado")
    else:
        print(row)


def run_everything(connection):
    answer = input("Indicar si quieres hacer INSERT, DELETE, SELECT o SELECTID: ").lower()
    while answer != "insert" and answer != "delete" and answer != "select" and answer != "selectid":
        print("Debes especificar una de las cuatro opciones")
        answer = input("Indicar si quieres hacer INSERT, DELETE, SELECT o SELECTID: ").lower()

    if answer == "insert":
        insert_data(connection)
    elif answer == "select":
        get_data(connection)
    elif answer == "selectid":
        get_data_by_id(connection)
    else:
        delete_data(connection)
        get_data(connection)


if __name__ == '__main__':
    conn = connection_database("localhost", "root", "root", "personas")
    run_everything(conn)
    conn.close()