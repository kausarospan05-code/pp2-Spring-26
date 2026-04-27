class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def total_salary(self):
        return float(self.salary)


class Manager(Employee):
    def __init__(self, name, salary, bonus_percent):
        super().__init__(name, salary)
        self.bonus_percent = bonus_percent

    def total_salary(self):
        return self.salary + (self.salary * self.bonus_percent / 100)


class Developer(Employee):
    def __init__(self, name, salary, projects):
        super().__init__(name, salary)
        self.projects = projects

    def total_salary(self):
        return self.salary + self.projects * 500


class Intern(Employee):
    pass   # Intern just uses base salary


data = input().split()
role = data[0]

if role == "Manager":
    name = data[1]
    salary = int(data[2])
    bonus = int(data[3])
    emp = Manager(name, salary, bonus)

elif role == "Developer":
    name = data[1]
    salary = int(data[2])
    projects = int(data[3])
    emp = Developer(name, salary, projects)

elif role == "Intern":
    name = data[1]
    salary = int(data[2])
    emp = Intern(name, salary)
print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")