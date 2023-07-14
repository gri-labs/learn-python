class Car:
    def __init__(self, make, model, year):
        self.mileage = None
        self.make = make
        self.model = model
        self.year = year

    def get_mileage(self):
        print("The car has {} miles on it.".format(self.mileage))

    def set_mileage(self, mileage):
        self.mileage = mileage


if __name__ == '__main__':
    kit = Car("Renault", "Megane", 2004)
    kit.set_mileage(120000)
    print(kit.get_mileage())
