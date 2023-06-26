class Users:
    def __init__(self, name, age, last_name):
        self.name = name
        self.age = age
        self.last_name = last_name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_lastname(self):
        return self.last_name

new_user = Users("Alhida", 18, "Llanos")

print(new_user.get_name())
print(new_user.get_age())
print(new_user.get_lastname())
