class Repository:
    def __init__(self, connector):
        self.connector = connector

    def get_users(self):
        return