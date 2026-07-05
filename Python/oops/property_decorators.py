# Q1 — First Property
from Python.data_structures.dictionaries import name


class Student:
    def __init__(self, marks):
        self._marks = marks
    @property
    def marks(self):
        return self._marks
    @marks.setter
    def marks(self, value):
        if value < 0:
            raise ValueError("Marks cannot be negative")
        self._marks = value
s = Student(85)
s.marks = 95
print(s.marks)
# s.marks = -20

# Q2 — Read-Only Property
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @property
    def area(self):
        return self.length * self.width
r = Rectangle(10, 5)
print(r.area)

# Q3 — Deleter
class Student:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.deleter
    def name(self):
        print("Student deleted")
        del self._name
s = Student("Banku")
print(s.name)
del s.name