class Service:
    def __init__ (self, repository):
        self.repository = repository

    def get_users(self):
        return self.repository.get_users()

    def get_user_by_id(self, id):
        return self.repository.get_user_by_id(id)

    def add_user(self, user):
        return self.repository.add_user(user)

    def update_user(self, user):
        return self.repository.update_user(user)