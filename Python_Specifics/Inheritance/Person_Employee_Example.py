class Person:
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname
    def get_name(self):
        return self.first_name + " " + self.last_name

class Employee(Person):
    def __init__(self, firstname, lastname, staff_num):
        # super.__init__() can also be used
        Person.__init__(self, firstname, lastname)
        self.staff_num = staff_num
    def get_employee(self):
        return self.get_name() + ", " + str(self.staff_num)

person = Person("Kaushik", "Sekar")
print("Person")
print(person.get_name())
emp = Employee("Kaushik", "Sekar", 318963)
print("Employee")
print(emp.get_name())
print(emp.get_employee())
