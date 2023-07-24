from student import Student


class Repository:
    def __init__(self, connector_database):
        self.connector = connector_database

    def get_student_by_id(self, user):
        return self.connector.execute_and_filter(Student, filter_by={'id': user.id})

    def add_user(self, user):
        self.connector.execute_and_commit(user)

    def delete_user(self, user):
        self.connector.delete_and_commit(user)
