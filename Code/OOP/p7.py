class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print("Name deleted")
        self.first = None
        self.last = None


emp1 = Employee("Areeb", "Shaik")
emp2 = Employee("Test", "user")

emp1.full_name = "Rafi Shaik"
print(emp1.full_name)

del emp1.full_name
print(emp1.full_name)   # None None
# print(emp1.email)
# print(emp1.full_name)
#
