class Repository:
    def __init__(self, connector):
        self.connector = connector

    def get_students(self):
        return self.connector.execute_and_fetchall("SELECT * FROM estudiantes")

    def get_student_by_id(self, id):
        # .format(id) es para que el id se ponga en el lugar de las llaves
        # y garantizar que la consulta se haga correctamente con el valor correcto.
        return self.connector.execute_and_fetchone("SELECT * FROM estudiantes WHERE id = {}".format(id))

    def get_students_by_name(self, name):
        return self.connector.execute_and_fetchall("SELECT * FROM estudiantes WHERE nombre = '{}'".format(name))

    def insert_student(self, name):
        return self.connector.execute_and_commit("INSERT INTO estudiantes (nombre) VALUES ('{}')".format(name))

    def update_student(self, id, nombre):
        return self.connector.execute_and_commit("UPDATE estudiantes SET nombre = '{}' WHERE id = {}".format(nombre, id))

    def delete_student(self, id):
        return self.connector.execute_and_commit("DELETE FROM estudiantes WHERE id = {}".format(id))
