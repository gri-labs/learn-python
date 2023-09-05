import math


class CalculateAreaOfCircle:
    def __init__(self, radius):
        self.radius = radius

    def calculate(self):
        return math.pi * self.radius ** 2
