from connector import ConnectorDatabase
import os

def split_file(file):
    return file.split(';')


if __name__ == '__main__':
    # read file .sql
    with open('empleados.sql', 'r') as file:
        file = file.read()

    # split file .sql
    file = split_file(file)

    # connect to database
    connect = ConnectorDatabase(
        host='localhost',
        user='root',
        password='root',
        database='mysql',
        port=3308
    )

    # execute file .sql
    for query in file:
        print(query)
        connect.execute_and_commit(query)
