class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_mileage(self):
        print("The car has {} miles on it.".format(self.mileage))

    def set_mileage(self, mileage):
        self.mileage = mileage


if __name__ == '__main__':

    my_car = Car('BMW', 'X6', 2022)

    my_car.set_mileage(2000)

    print(my_car.make)
    print(my_car.model)
    print(my_car.year)
    my_car.get_mileage()