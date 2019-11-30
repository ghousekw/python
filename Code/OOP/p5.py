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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prg_lng):
        super().__init__(first, last, pay)  # Employee.__init__(self,first,last,pay) also same
        self.prg_lng = prg_lng


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.full_name())


dev_1 = Developer("Areeb", "Shaik", 20000, 'python')
dev_2 = Developer("Test", "user", 30000, 'java')

mgr_1 = Manager("John", "Smith", 100000, [dev_1])

# print(isinstance(mgr_1, Manager))  # True
# print(isinstance(mgr_1, Employee))  # True
# print(isinstance(mgr_1, Developer))  # False

print(issubclass(Developer, Employee)) # True
print(issubclass(Developer, Manager)) # False
print(issubclass(Manager, Developer)) # False
# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.remove_emp(dev_2)
# mgr_1.print_emp()
# print(dev_1.email)
# print(dev_1.prg_lng)
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# print(help(Developer))
