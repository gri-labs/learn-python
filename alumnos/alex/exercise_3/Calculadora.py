class Calculo(object):
    def __init__(self):

    def suma_primeros_naturales(self, num):
        i = 0
        sum = 0
        while i <= num:
            sum = sum + i
            i = i + 1
        return sum

thing = Calculo()
print(thing.suma_primeros_naturales(8))

