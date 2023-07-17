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
    # TODO: Imprimir los valores de las
    myCar = Car("Mazda", "CX-5", 2022)

    myCar.set_mileage(2000)

    print("Make:", myCar.make)
    print("Model:", myCar.model)
    print("Year:", myCar.year)
    myCar.get_mileage()
