# Q1 — Method Overriding
class Vehicle:
    def start(self):
        print("Vehicle Started")
class Car(Vehicle):
    def start(self):
        super().start()
        print("Car Started")
c = Car()
c.start()

# Encapsulation Practice
# Q2 — Public Attribute
class Student:
    def __init__(self, name):
        self.name = name
s = Student("Banku")
print(s.name)

# Q3 — Protected Attribute
class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks
    def show_marks(self):
        print(self._marks)
s = Student("Banku", 85)
print(s.name)
s.show_marks()
print(s._marks)

# Q4 — Private Attribute
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
e = Employee("Banku", 50000)
# print(e.__salary)
# AttributeError: 'Employee' object has no attribute '__salary'
print(e._Employee__salary)