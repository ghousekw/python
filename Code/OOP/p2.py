class Employee:
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"

        Employee.num_of_emp += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# Before Instantiated Class Employee
print(Employee.num_of_emp)

emp1 = Employee("Areeb", "Shaik", 20000)
emp2 = Employee("Test", "user", 30000)

# After Instantiated Class Employee
print(Employee.num_of_emp)
# print(emp1.__dict__)
# # print(Employee.__dict__)
# print(Employee.raise_amount)  # prints the class variable value
# # Changing emp1 raise_amount
# emp1.raise_amount = 1.08
# print(emp1.__dict__)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
