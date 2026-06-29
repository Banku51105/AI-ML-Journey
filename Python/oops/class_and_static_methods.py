# Q1 — Class Variable Counter
class Student:
    total_students = 0
    def __init__(self, name):
        self.name = name
        Student.total_students += 1
    @classmethod
    def get_total_students(cls):
        return cls.total_students
s1 = Student("Banku")
print(s1.name)
s2 = Student("Gunjan")
s3 = Student("Rupali")
print(Student.get_total_students())

# Q2 — Change School
class Students:
    school = "ABC School"
    def __init__(self, name):
        self.name = name
    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name
s1 = Students("Banku")
s2 = Students("Gunjan")
s3 = Students("Rupali")
print(Students.school)
Students.change_school("XYZ")
print(Students.school)

# Q3 — Static Calculator
class Calculator:
    @staticmethod
    def add(a,b):
        return a + b
    @staticmethod
    def sub(a,b):
        return a - b
print(Calculator.add(2,3))
print(Calculator.sub(3,2))

# Q4 — Temperature Converter
class Converter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9
print(Converter.celsius_to_fahrenheit(0))
print(Converter.fahrenheit_to_celsius(32))

# Q5
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @classmethod
    def from_string(cls, data):
        name, marks = data.split(",")
        return cls(name, int(marks))
s = Student.from_string("Banku,85")
print(s.name)
print(s.marks)