class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def change_salary(self, new_salary):
        self.salary = new_salary


if __name__ == '__main__':
    employee = Employee('John', 1000)
    print(employee.get_salary())
    employee.change_salary(2000)
    print(employee.get_salary())
