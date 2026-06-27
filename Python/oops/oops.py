# Question 1 — Student Age
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
s1 = Student("Banku",21)
s1.show_details()
s2 = Student("Gunjan",19)
s2.show_details()

# Question 2 — Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
r1 = Rectangle(10, 5)
print(r1.area())

# Question 3 — Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_salary(self):
        return f"{self.name} earns {self.salary}"
e1 = Employee("Rahul", 50000)
print(e1.show_salary())

# Question 4 — Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
c1 = Circle(5)
print(c1.area())

# Question 5 — Bank Account
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def show_balance(self):
        return f"{self.name} has {self.balance}"
b1 = BankAccount("Banku",5000)
print(b1.show_balance())

# Question 6 — Student Marks Update
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
    def update_marks(self, new_marks):
        self.marks = new_marks
s1 = Student("Banku", 85)
s1.show_details()
s1.update_marks(95)
s1.show_details()

# Question 7 — Bank Account Deposit & Withdraw
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        self.balance -= amount
    def show_balance(self):
        return f"{self.name} has {self.balance}"
b1 = BankAccount("Banku", 5000)
b1.deposit(1000)
print(b1.show_balance())
b1.withdraw(2000)
print(b1.show_balance())

# Question 8 — Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return (self.length + self.width) * 2
r1 = Rectangle(10, 5)
print(r1.area())
print(r1.perimeter())

# Question 9 — Employee Salary Hike
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def increase_salary(self, amount):
        self.salary += amount
    def show_salary(self):
        return f"{self.name} earns {self.salary}"
e1 = Employee("Rahul", 50000)
e1.increase_salary(5000)
print(e1.show_salary())

# Q10 — Student Grade & Pass/Fail & Report
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
    def update_marks(self, new_marks):
        self.marks = new_marks
    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"
    def is_pass(self):
        return self.marks >= 40
    def report(self):
        return {"Name" : self.name, "Marks" : self.marks, "Grade" : self.get_grade(), "Pass" : self.is_pass()}
s1 = Student("Banku", 85)
print(s1.get_grade())
print(s1.is_pass())
print(s1.report())

# Q11 — Bank Account Transfer
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        self.balance -= amount
    def transfer(self,other_account,amount):
        other_account.balance += amount
        self.balance -= amount
    def show_balance(self):
        return f"{self.name} has {self.balance}"
banku = BankAccount("Banku", 5000)
rahul = BankAccount("Rahul", 2000)
banku.transfer(rahul, 1000)
rahul.transfer(banku, 2000)
print(banku.show_balance())
print(rahul.show_balance())

# Q12 — Employee Bonus
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def increase_salary(self, amount):
        self.salary += amount
    def give_bonus(self, percent):
        self.salary += self.salary * percent / 100
    def show_salary(self):
        return f"{self.name} earns {self.salary}"
e1 = Employee("Banku",50000)
e1.give_bonus(20)
print(e1.show_salary())

# Q13 — Circle Comparison
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def bigger_than(self,other_circle):
        if self.area() > other_circle.area():
            return True
        else:
            return False
c1 = Circle(5)
c2 = Circle(3)
print(c1.bigger_than(c2))

# Q14 — Student Comparison
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
    def update_marks(self, new_marks):
        self.marks = new_marks
    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"
    def has_higher_marks(self,other_student):
        return self.marks > other_student.marks
    def is_pass(self):
        return self.marks >= 40
    def report(self):
        return {"Name" : self.name, "Marks" : self.marks, "Grade" : self.get_grade(), "Pass" : self.is_pass()}
s1 = Student("Banku", 85)
s2 = Student("Gunjan", 95)
print(s1.has_higher_marks(s2))

# Q15 — Bank Account Validation
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient Balance")
        else:
            self.balance -= amount
    def transfer(self,other_account,amount):
        if self.balance >= amount:
            other_account.balance += amount
            self.balance -= amount
        else:
            print("Insufficient Balance")
    def show_balance(self):
        return f"{self.name} has {self.balance}"
b1 = BankAccount("Banku", 5000)
b1.deposit(1000)
print(b1.show_balance())
b1.withdraw(7000)
print(b1.show_balance())
banku = BankAccount("Banku", 5000)
rahul = BankAccount("Rahul", 2000)
banku.transfer(rahul, 7000)

# Q16 — Mini OOP Challenge
class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available
    def borrow_book(self):
        if self.available:
            print(f"Borrowed {self.title} by {self.author}")
            self.available = False
        else:
            print("Book Not Available")
    def return_book(self):
        print(f"Returned {self.title} by {self.author}")
        self.available = True
    def show_status(self):
        print(self.available)
book1 = Book("Deep Work", "Cal Newport", True)
book1.borrow_book()
book1.borrow_book()
book1.show_status()

# Q17 — Library Management System
class Book:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability
    def borrow_book(self):
        if self.availability:
            print(f"Borrowed {self.title} by {self.author}")
            self.availability = False
        else:
            print("Book Not Available")
    def return_book(self):
        print(f"Returned {self.title} by {self.author}")
        self.availability = True
    def show_status(self):
        print(f"{self.title} by {self.author} is {'Available' if self.availability else 'Not Available'}")

class Library:
    def __init__(self, books):
        self.books = books
    def add_book(self, book):
        self.books.append(book)
    def show_books(self):
        for book in self.books:
            book.show_status()
book1 = Book("Deep Work", "Cal Newport", True)
book2 = Book("Atomic Habits", "James Clear", True)
library = Library([])
library.add_book(book1)
library.add_book(book2)
library.show_books()
book1.borrow_book()
library.show_books()
