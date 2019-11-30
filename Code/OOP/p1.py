class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"

    def full_name(self):
        return f"{self.first} {self.last}"


emp1 = Employee("Areeb", "Shaik", 20000)
emp2 = Employee("Test", "user", 30000)

print(emp1.email)

#   printing by using instance
print(emp1.full_name())
print(emp2.full_name())

# Printing by class
print(Employee.full_name(emp1))


# print(f"{emp1.first} {emp1.last}")


#
# emp1.first = "Areeb"
# emp1.last = "shaik"
# emp1.email = "Areeb.shaik@gmail.com"
# emp1.pay = 50000
#
# emp2.first = "Test"
# emp2.last = "User"
# emp2.email = "Test.User@gmail.com"
# emp2.pay = 60000
#
# print(emp1.first)
# print(emp1.last)
# print(emp1.email)
# print(emp1.pay)
#
# print(emp2.first)
# print(emp2.last)
# print(emp2.email)
# print(emp2.pay)
