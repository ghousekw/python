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

# Creating Class Methods
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# Creating alternative class method
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str_1.split('-')
        return cls(first, last, pay)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-50000"
emp_str_3 = "Rose-Mary-80000"

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

# emp1 = Employee("Areeb", "Shaik", 20000)
# emp2 = Employee("Test", "user", 30000)

# print(emp1.raise_amount)
# print(emp2.raise_amount)
#
# # By using class methods
# # Employee.set_raise_amount(2.04)
# # By using class instances
# emp1.set_raise_amount(2.05)
# print(emp1.raise_amount)
# # Although we set_raise_amount to emp1 it will also applicable to emp2 instances
# print(emp2.raise_amount)