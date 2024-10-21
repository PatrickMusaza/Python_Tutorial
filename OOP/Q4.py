class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def give_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)
        print(f"{self.name}'s new salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, "Manager", salary)

class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, "Developer", salary)

# Create objects and test
manager = Manager("Eve", 90000)
developer = Developer("Patrick", 75000)

manager.give_raise(10)
developer.give_raise(5)
