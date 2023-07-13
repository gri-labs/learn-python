class Users:
    def __init__(self, name, age, last_name):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_last_name(self):
        return self.last_name


student = Users('Ricardo', 25)
print(student.get_name())
print(student.get_age())
print(student.get_last_name('García'))