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
    # TODO: Asignar valores a las variables
    # TODO: Imprimir los valores de las variables
    coche_1 = Car("Seat", "Leon", "2018")
    coche_1.set_mileage(100000)
    coche_1.get_mileage()
    print(coche_1.make)
    print(coche_1.model)
    print(coche_1.year)