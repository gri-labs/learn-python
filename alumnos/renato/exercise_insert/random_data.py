import random


class RandomData:

    def __init__(self):
        self.appellidos = ['Pepe', 'Pedro', 'Juanjo', 'Gimmy', 'Sanchez']
        self.emails = ['renato@gmail.com', 'loida@hotmail.com', 'Merlin@cat.com', 'Ginger@cat1.com', 'Nata@cat2.com']
        self.nombres = ['Renato', 'Loida', 'Merlin', 'Ginger', 'Nata']

    def random_name(self):
        return random.choice(self.nombres) + str(random.randint(0, 1000))

    def random_surname(self):
        return random.choice(self.appellidos) + " " + str(random.randint(0, 1000))

    def random_email(self):
        return str(random.randint(0, 1000)) + random.choice(self.emails)

    def random_edad(self):
        return random.randint(18, 60)
