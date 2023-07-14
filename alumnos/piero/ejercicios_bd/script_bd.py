import random
from faker import Faker
import mysql.connector


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


class DBOperator:
    def __init__(self, connection):
        self.connection = connection
        self.fake = Faker(['it_IT', 'es_ES', 'en_US'])

    def gen_correo_electronico(self, nombre, apellido):
        proveedor = self.fake.free_email_domain()
        correo_electronico = f"{nombre}.{apellido}@{proveedor}"
        return correo_electronico

    def gen_nombre(self):
        nombre = self.fake.first_name()
        return nombre

    def gen_apellido(self):
        apellido = self.fake.last_name()
        return apellido

    def gen_edad(self):
        edad = random.randint(18, 65)
        return edad

    def insert_data(self):
        for i in range(1, 100000):
            correo_electronico = self.gen_correo_electronico(self.gen_nombre(), self.gen_apellido())
            nombre = self.gen_nombre()
            apellido = self.gen_apellido()
            edad = self.gen_edad()
            cursor_commit_query(self.connection, f"INSERT INTO usuarios (email, nombre, apellido, edad) VALUES ('{correo_electronico}', '{nombre}', '{apellido}', {edad})")

    def delete_data(self):
        cursor_commit_query(self.connection, "DELETE FROM usuarios")

    def get_data(self):
        rows = execute_query("SELECT * FROM usuarios", self.connection)
        if len(rows) == 0:
            print("No hay registros")
        else:
            for row in rows:
                print(row)

    def get_data_by_id(self):
        id = int(input("Indica qué ID quieres buscar: "))
        row = execute_query(f"SELECT * FROM usuarios WHERE id = {id}", self.connection)
        if len(row) == 0:
            print("ID no encontrado")
        else:
            print(row)

    def run_everything(self):
        answer = input("Indica si quieres hacer INSERT, DELETE, SELECT o SELECTID: ").lower()
        while answer not in ["insert", "delete", "select", "selectid"]:
            print("Debes especificar una de las cuatro opciones")
            answer = input("Indica si quieres hacer INSERT, DELETE, SELECT o SELECTID: ").lower()

        if answer == "insert":
            self.insert_data()
        elif answer == "delete":
            self.delete_data()
            self.get_data()
        elif answer == "select":
            self.get_data()
        elif answer == "selectid":
            self.get_data_by_id()

if __name__ == '__main__':
    conn = connection_database("localhost", "root", "root", "personas")
    operator = DBOperator(conn)
    operator.run_everything()
    conn.close()