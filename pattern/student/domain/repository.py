class StudentRepository:
    def __init__(self, connector_database):
        self.connector = connector_database

    def get_student_by_id(self, model_data, id):
        result = self.connector.get_by_id(model_data, id)

        return result
