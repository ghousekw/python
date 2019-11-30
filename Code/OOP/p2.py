class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = self.pay * 1.04


emp1 = Employee("Areeb", "Shaik", 20000)
emp2 = Employee("Test", "user", 30000)

print(emp1.email)

#   printing by using instance
print(emp1.full_name())
print(emp2.full_name())

# Printing by class
print(Employee.full_name(emp1))

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)