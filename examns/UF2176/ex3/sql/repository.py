class Repository:
    def __init__(self, connector):
        self.connector = connector
    
    def get_user_by_id(self, id):
        return self.connector.execute_and_fetchone("SELECT * FROM user WHERE id = {}".format(id))
    
    def insert_user(self, id, nombre, edad):
        return self.connector.execute_and_commit("INSERT INTO user (id, nombre, edad) VALUES ('{}', '{}', '{}')".format(id, nombre, edad))