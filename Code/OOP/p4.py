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

    # Creating Static Methods
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-50000"
emp_str_3 = "Rose-Mary-80000"

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

import datetime

my_date = datetime.date(2019, 11, 30)
print(Employee.is_workday(my_date))
