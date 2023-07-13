class Calc(object):
    def __init__(self, num):
        self.num = num

    def suma_first_naturals(self):
        i = 0
        result = 0
        while i <= self.num:
            result = result + i
            i = i + 1
        return result


thing = Calc(22)
print(thing.suma_first_naturals())
