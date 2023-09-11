class StudentRepository:
    def __init__(self, connector_database):
        self.connector = connector_database

    def get_student_by_id(self, model_data, student_id):
        return self.connector.get_by_id(model_data, student_id)

    def add_student(self, student):
        return self.connector.add(student)