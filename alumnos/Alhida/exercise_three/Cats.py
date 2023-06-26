class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def meow(self):
        return "Meow!"

    def information(self):
        return f"Name: {self.name}\nAge: {self.age}\nColor: {self.color}"
