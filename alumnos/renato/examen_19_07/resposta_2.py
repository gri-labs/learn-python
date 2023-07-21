# Una clase Employee que tenga los atributos name y salary. La clase también debe tener un método get_salary() que
# devuelva el salario del empleado y un método change_salary() que cambie el salario del empleado. Genera la base del
# script, con (if  __name__) , donde instancies la clase y uses los métodos declarados.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def change_salary(self, new_salary):
        self.salary = new_salary


if __name__ == '__main__':
    employee = Employee("Renato", 5000)

    print("Primer salario:", employee.get_salary())

    employee.change_salary(6000)

    print("Secundo salario:", employee.get_salary())
