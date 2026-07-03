class Employee:
    company ="Apple"
    def  __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role
class programmer(Employee):
    def __init__(self,name,salary,role,languages):
        super().__init__(name,salary,role)
        self.languages = languages

# e = Employee("John", 50000, "Developer")
# print(e.name)
# print(e.salary)
# print(e.role)

p = programmer("Jane", 60000, "Programmer", ["Python", "Java"])
print(p.name)
print(p.salary)
print(p.role)
print(p.languages)