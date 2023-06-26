class Auto:
    def __init__(self, model, power, speed):
        self.model = model
        self.power = power
        self.speed = speed

    def get_model(self):
        return self.model

    def get_power(self):
        return self.power

    def get_speed(self):
        return self.speed

    def get_speed_per_power(self):
        return self.power / self.speed


myCar = Auto("Renault", 2400, 190)

print(myCar.get_speed_per_power())
