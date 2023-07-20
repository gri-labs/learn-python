class Repository:
    def __init__(self, connector):
        self.connector = connector

    def get_users(self):
        return self.connector.execute_query("SELECT * FROM alumnos")

    # TODO: Implement get user by id

    # TODO: Implement create user

    # TODO: Implement update user

    # TODO: Implement delete user