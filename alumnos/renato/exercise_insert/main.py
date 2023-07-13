import mysql.connector
import random
import time

appellidos = ['Pepe', 'Pedro', 'Juanjo', 'Gimmy', 'Sanchez']
emails = ['renato@gmail.com', 'loida@hotmail.com', 'Merlin@cat.com', 'Ginger@cat1.com', 'Nata@cat2.com']
nombres = ['Renato', 'Loida', 'Merlin', 'Ginger', 'Nata']


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
    print(t1-t0)
    return results


def insert_data():
    for i in range(100000):
        user_name = random_name()
        email = random_email()
        appellido = random_surname()
        edad = random.randint(18, 60)

        sql_code = f"""
        INSERT INTO users (nombre, email, appellido, edad)
        VALUES ('{user_name}', '{email}',  '{appellido}', '{edad}')
        """
        exec_and_commit(sql_code)


def random_surname():
    return random.choice(appellidos) + " " + str(random.randint(0, 1000))


def random_email():
    return str(random.randint(0, 1000)) + random.choice(emails)


def random_name():
    return random.choice(nombres) + str(random.randint(0, 1000))


def delete_data():
    sql_code = "DELETE FROM users;"
    exec_and_commit(sql_code)


if __name__ == '__main__':
    connection_db = connection_database('localhost', 'root', 'root', 3307, 'usuarios')
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

            print("NO STUDENT IS PRESENT WITH THAT ID")

    elif name.upper() == "SEARCHFIELD":
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

    connection_db.close()
