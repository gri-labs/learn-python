import mysql.connector
import time

from random_data import RandomData

data = RandomData()

def connection_database(host, user, password, port, database_name):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=int(port),
        database=database_name,
    )
    return connection


def exec_and_commit(query):
    cursor = connection_db.cursor()
    cursor.execute(query)
    connection_db.commit()
    cursor.close()


def execute_query_select(query):
    t0 = time.time()
    cursor = connection_db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    t1 = time.time()
    print(t1 - t0)
    return results


def insert_data():
    for i in range(10):
        estudiante = data
        user_name = estudiante.random_name()
        email = estudiante.random_email()
        appellido = estudiante.random_surname()
        edad = estudiante.random_edad()

        sql_code = f"""
        INSERT INTO users (nombre, email, appellido, edad)
        VALUES ('{user_name}', '{email}',  '{appellido}', '{edad}')
        """
        exec_and_commit(sql_code)


def delete_data():
    sql_code = "DELETE FROM users;"
    exec_and_commit(sql_code)


def check_action(action):
    if action.upper() == "INSERT":
        insert_data()

    elif action.upper() == "DELETE":
        delete_data()

    elif action.upper() == "SEARCHID":
        search_id = input("Which id? ")
        sql_code = f"""
        SELECT * FROM users WHERE id='{search_id}'"""
        rows = execute_query_select(sql_code)

        if len(rows) > 0:
            print(rows)

        else:
            print("NO STUDENT IS PRESENT WITH THAT ID")

    elif action.upper() == "SEARCHFIELD":
        search_field = input("Which field? ")
        search_valor = input("What are you searching for? ")
        sql_code = f"""
        SELECT * FROM users WHERE {search_field}='{search_valor}'"""
        rows = execute_query_select(sql_code)

        if len(rows) > 0:
            print(rows)

        else:
            print("NO RESULT FOR YOUR SEARCH")

    else:
        print("Action not valid")


if __name__ == '__main__':
    connection_db = connection_database('localhost', 'root', 'root', 3307, 'usuarios')
    action = input("Which action? ")
    check_action(action)
    connection_db.close()
