class Repository:
    def __init__(self, connector):
        self.connector = connector

    def get_users(self, user_id):
        return self.users.get(user_id)

    def insert_user(self, user_id, user_name):
        user = {"id": user_id, "name": user_name}
        self.users.append(user)