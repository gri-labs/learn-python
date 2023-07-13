import mysql.connector
from flask import jsonify
import random


def connection_database(database_name):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        port=int(3307),
        database=database_name,
    )
    return connection


def exec_and_commit(query):
    cursor = connection_db.cursor()
    cursor.execute(query)
    connection_db.commit()
    cursor.close()


def execute_query_select(query):
    cursor = connection_db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def insert_data():
    nombres = ['Renato', 'Loida', 'Merlin', 'Ginger', 'Nata']
    emails = ['renato@gmail.com', 'loida@hotmail.com', 'Merlin@cat.com', 'Ginger@cat1.com', 'Nata@cat2.com']
    appellidos = ['Pepe', 'Pedro', 'Juanjo', 'Gimmy', 'Sanchez']

    for i in range(10000):
        user_name = random.choice(nombres) + str(random.randint(0, 1000))
        email = str(random.randint(0, 1000)) + random.choice(emails)
        appellido = random.choice(appellidos) + " " + str(random.randint(0, 1000))
        edad = random.randint(18, 60)

        sql_code = f"""
        INSERT INTO users (nombre, email, appellido, edad)
        VALUES ('{user_name}', '{email}',  '{appellido}', '{edad}')
        """
        exec_and_commit(sql_code)


def delete_data():
    sql_code = "DELETE FROM users;"
    exec_and_commit(sql_code)


if __name__ == '__main__':
    connection_db = connection_database('usuarios')
    name = input("Which action? ")
    if name.upper() == "INSERT":
        insert_data()
    elif name.upper() == "DELETE":
        delete_data()
    elif name.upper() == "SEARCHID":
        search_id = input("Which id? ")
        sql_code = f"""
        SELECT * FROM users WHERE id='{search_id}'"""
        rows = execute_query_select(sql_code)
        if len(rows) > 0:
            print(rows)
        else:
            print("ESTUDIANTE NO ENCONTRADO")

# elif name.upper() == "SEARCHFIELD":

    connection_db.close()
