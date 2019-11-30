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

    # Representation
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    # Presentation
    def __str__(self):
        return f"{self.full_name()} - {self.email}"

    # Combining two emp salaries
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())

emp1 = Employee("Areeb", "Shaik", 20000)
emp2 = Employee("Test", "user", 30000)

# print(emp1)
# print(emp1.__repr__())  # print(repr(emp1))
# print(emp1.__str__())  # print(str(emp1))
# print(int.__add__(1, 2))    # 3
# print(str.__add__('a', 'b'))    # ab
# print(emp1 + emp2) # 50000
# print(len('test'))  # or print('test'.__len__())    # 4
print(len(emp1))    # 11
