from connector_database import ConnectorDatabase

conn = ConnectorDatabase()

class Repository:
    def __init__(self, connector):
        self.connector = connector

    def get_users(self, user_id):
        query = "SELECT * FROM users WHERE id = %s;" % user_id
        result = execute_and_fetchone(query)
        return self.uers.get(result)

    def insert_user(self, user_id, user_name):
        user = {"id": user_id, "name": user_name}
        self.users.append(user)