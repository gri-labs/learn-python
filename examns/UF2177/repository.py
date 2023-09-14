class Repository:
    def __init__(self, connector_database):
        self.connector = connector_database

    def get_student_by_id(self, user_id):
        query = f"SELECT * FROM student WHERE id = {user_id}"
        result = self.connector.connector_database(query)
        return result


