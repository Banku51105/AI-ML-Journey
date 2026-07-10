# Q1 — Student Management
class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self._marks}")
    @property
    def marks(self):
        return self._marks
    @marks.setter
    def marks(self, value):
        if value < 0:
            raise ValueError("Marks cannot be negative")
        self._marks = value
    @property
    def grade(self):
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
student = Student("Banku", 85)
print(student.grade)
student.marks = 95
print(student.grade)

# Q2 — Wallet Comparison
class Wallet:
    def __init__(self, owner, money):
        self.owner = owner
        self.money = money
    def __str__(self):
        return f"Owner: {self.owner}, Money: {self.money}"
    def __add__(self, other):
        return self.money + other.money
    def __gt__(self, other):
        return self.money > other.money
w1 = Wallet("Banku", 500)
w2 = Wallet("Rahul", 300)
print(w1)
print(w1 + w2)
print(w1 > w2)

# Q3 — Library System
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

# Q4 — Employee Management
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be Negative")
        self._salary = value
    def __str__(self):
            return f"{self.name} earns {self.salary}"
e = Employee("Banku", 50000)
print(e.salary)
e.salary = 60000
print(e)

# Q5 — Bank System
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self.balance += amount
        print(f"{amount} Deposited to Account\nBalance: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} Withdrawn from Account\nBalance: {self.balance}")
        else:
            print(f"Insufficient Balance\nBalance: {self.balance}")
    def transfer(self, other_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"{amount} Transferred from account\nBalance: {self.balance}")
        else:
            print(f"Insufficient Balance\nBalance: {self.balance}")
    def __str__(self):
        return f"{self.account_holder} has {self.balance}"
account1 = BankAccount("Banku",50000)
print(account1)
account2 = BankAccount("Gunjan", 50000)
print(account2)
account2.deposit(1000)
account2.withdraw(1000)
account1.transfer(account2, 10000)

# Q6 — Shape System
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
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
shapes = [Rectangle(5,2), Circle(5)]
for shape in shapes:
    name = shape.__class__.__name__
    print(f"Area of {name}: {shape.area()}")

# Q7 — Shopping Cart
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"
class ShoppingCart:
    def __init__(self):
        self.products = []
    def add_product(self, product):
        self.products.append(product)
    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                break
    @property
    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
product1 = Product("Chocolate", 50)
product2 = Product("Chips", 40)
cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)
print(cart.total_price)
cart.remove_product("Chips")
print(cart.products)
print(cart.total_price)

# Q8 — University
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
    @property
    def status(self):
        return "Pass" if self.marks >= 40 else "Fail"
student = Student("Banku", 21, 85)
print(student.status)

# Q9 — Team
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __gt__(self, other):
        return self.score > other.score
    def __repr__(self):
        return f"Player(name='{self.name}', score={self.score})"
class Team:
    def __init__(self):
        self.players = []
    def add_players(self, player):
        self.players.append(player)
    def best_player(self):
        if not self.players:
            return None
        best = self.players[0]
        for player in self.players:
            if player > best:
                best = player
        return best
my_team = Team()
p1 = Player("Alice", 90)
p2 = Player("Bob", 95)
my_team.add_players(p1)
my_team.add_players(p2)
print(my_team.players)
print(my_team.best_player())

# Q10 — File Logger (Decorators)
from functools import wraps
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper
@logger
def add(a, b):
    return a + b
print(add(5,6))

# Q11 — Bank (Composition)
class Customer:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Customer('{self.name}')"
class Bank:
    def __init__(self):
        self.customers = []
    def add_customer(self, customer):
        self.customers.append(customer)
    def show_customers(self):
        print(f"Current bank customers: {self.customers}")
my_bank = Bank()
alice = Customer("Alice")
bob = Customer("Bob")
my_bank.add_customer(alice)
my_bank.add_customer(bob)
my_bank.show_customers()