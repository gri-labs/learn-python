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
    # TODO: Crear un objeto de tipo Car
    car = Car("Ford", "Fiesta", 2019)
    # TODO: Asignar valores a las variables
    car.set_mileage(23000)
    # TODO: Imprimir los valores de las variables
    car.get_mileage()
