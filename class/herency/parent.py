# parent class
class Parent:
    # parent class method
    def m1(self):
        print('Parent Class Method called...')


# child class inheriting parent class
class Child(Parent):
    # child class constructor
    def __init__(self):
        print('Child Class object created...')

    # child class method
    def m2(self):
        print('Child Class Method called...')


# creating object of child class
obj = Child()
# calling parent class m1() method
obj.m1()
# calling child class m2() method
obj.m2()
