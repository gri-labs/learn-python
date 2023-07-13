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


def GenCorreoElectronico(Nombre, Apellido):
    proveedor = fake.free_email_domain()
    CorreoElectronico = f"{Nombre}.{Apellido}@{proveedor}"
    return CorreoElectronico


def GenNombre():
    Nombre = fake.first_name()
    return Nombre


def GenApellido():
    Apellido = fake.last_name()
    return Apellido


def GenEdad():
    Edad = random.randint(18, 65)
    return Edad


def insert_data(connection):
    for i in range(1, 10):
        CorreoElectronico = GenCorreoElectronico(GenNombre(), GenApellido())
        Nombre = GenNombre()
        Apellido = GenApellido()
        Edad = GenEdad()
        cursor_commit_query(connection, f"INSERT INTO usuarios (email, nombre, apellido, edad) VALUES ('{CorreoElectronico}', '{Nombre}', '{Apellido}', {Edad})")


def delete_data(connection):
    cursor_commit_query(connection, "DELETE FROM usuarios")


def get_data(connection):
    rows = execute_query("SELECT * FROM usuarios", connection)
    for row in rows:
        print(row)


def get_data_by_id(connection):
    row = execute_query("SELECT * FROM usuarios ORDER BY id DESC LIMIT 1", connection)
    print(row)


def run_everything(connection):
    answer = input("Indicar si quieres hacer INSERT o DELETE: ").lower()
    while answer != "insert" and answer != "delete":
        print("Debes especificar una de las dos opciones (insert o delete)")
        answer = input("Indicar qué quieres hacer: ").lower()

    if answer == "insert":
        insert_data(connection)
        get_data(connection)
        get_data_by_id(connection)
    elif answer == "delete":
        delete_data(connection)
        get_data(connection)


if __name__ == '__main__':
    conn = connection_database("localhost", "root", "root", "personas")
    run_everything(conn)
    conn.close()