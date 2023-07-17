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
    carro = Car('Toyota', 'Yaris', 2000)
    print(carro.make)
    print(carro.model)
    print(carro.year)
