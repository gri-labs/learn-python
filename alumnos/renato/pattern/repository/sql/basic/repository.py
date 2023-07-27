class Repository:
    def __init__(self, connector):
        self.connector = connector

    def get_students(self):
        return self.connector.execute_and_fetchall("SELECT * FROM estudiantes")

    def get_student_by_id(self, student_id):
        return self.connector.execute_and_fetchone(f"SELECT * FROM estudiantes WHERE id = '{student_id}'")

    def get_students_by_name(self, student_name):
        return self.connector.execute_and_fetchall(f"SELECT * FROM estudiantes WHERE nombre = '{student_name}'")

    def insert_student(self, nombre, email, appellido, edad):
        sql = f"""INSERT INTO estudiantes (nombre, email, appellido, edad) VALUES ('{nombre}', '{appellido}','{email}', '{edad}')"""
        self.connector.add(sql)

    def update_student(self, id, nombre):
        sql = f"UPDATE estudiantes SET nombre = '{nombre}' WHERE id = '{id}'"
        self.connector.add(sql)

    def delete_student(self, id):
        sql = f"DELETE FROM estudiantes WHERE id = '{id}'"
        self.connector.add(sql)
