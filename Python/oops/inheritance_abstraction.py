# Q1 — Dog Inheritance
class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("Barking")
d = Dog()
d.eat()
d.bark()

# Q2 — Cat Inheritance
class Animal:
    def eat(self):
        print("Eating")
class Cat(Animal):
    def meow(self):
        print("Meow")
c = Cat()
c.eat()
c.meow()

# Q3 — Vehicle Inheritance
class Vehicle:
    def start(self):
        print("Vehicle Started")
class Car(Vehicle):
    def drive(self):
        print("Driving Car")
c = Car()
c.start()
c.drive()

# Q4 — Employee Inheritance
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_details(self):
        print("Name:", self.name)
        print("Salary", self.salary)
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
m = Manager("Banku", 50000, "IT")
m.show_details()

# Q5 — isinstance()
class Animal:
    pass
class Dog(Animal):
    pass
d = Dog()
print(isinstance(d, Dog))
print(isinstance(d, Animal))

# Q6 — Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_person(self):
        print(f"Name:{self.name} Age:{self.age}")
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
    def show_student(self):
        print(f"Name:{self.name}\nAge:{self.age}\nMarks:{self.marks}")
s = Student("Banku", 21, 85)
s.show_student()

# Q7 — Multiple Inheritance
class Father:
    def skill1(self):
        print("Driving")
class Mother:
    def skill2(self):
        print("Cooking")
class Child(Father,Mother):
    pass
c = Child()
c.skill1()
c.skill2()

# Q8 — Multilevel Inheritance
class GrandParent:
    def wisdom(self):
        print("Wise Advice")
class Parent(GrandParent):
    def work(self):
        print("Working")
class Child(Parent):
    def play(self):
        print("Playing")
c = Child()
c.wisdom()
c.work()
c.play()

# Q9 — First Abstract Class
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
r = Rectangle(2,4)
print(r.area())

# Q10 — Animal Sounds
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
d = Dog()
d.sound()
c = Cat()
c.sound()

# Q11 — Employee Salary
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self,monthly_salary):
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary
class FreelanceEmployee(Employee):
    def __init__(self, hours_worked,hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
s1 = FullTimeEmployee(50000)
print(s1.calculate_salary())
s2 = FreelanceEmployee(10,100)
print(s2.calculate_salary())