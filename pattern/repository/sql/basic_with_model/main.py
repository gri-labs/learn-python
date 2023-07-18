import mysql.connector
from connector_database import ConnectorDatabase


class Student:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class Repository:
    def __init__(self, connection):
        self.connection = connection

    def get_users(self):
        students = []
        results = self.connection.execute_query("SELECT * FROM alumnos")
        for result in results:
            students.append(Student(result[0], result[1], result[2]))
        return students

    def get_user(self, id):
        return self.connection.execute_query("SELECT * FROM alumnos WHERE id = %s" % id)

    # TODO: Implement create user

    # TODO: Implement update user

    # TODO: Implement delete user


if __name__ == '__main__':
    # TODO: Instance the repository with the connector

    # TODO: Get all users

    # TODO: Implement a class to print data
    # TODO: Print users

    # TODO: Get user by id

    # TODO: Create a new user

    # TODO: Update user

    # TODO: Delete user


