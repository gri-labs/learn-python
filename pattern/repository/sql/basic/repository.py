class Repository:
    def __init__(self, connector):
        self.connector = connector

    def get_students(self):
        return self..("SELECT * FROM estudiantes")

    def get_student_by_id(self, ):
        return self..("")

    def get_students_by_name(self, ):
        return self..execute_and_fetchall()

    def insert_student(self, ):

    def update_student(self, id, nombre):

    def delete_student(self, id):
