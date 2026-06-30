# Q1 — __str__
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def __str__(self):
        return f"{self.name} by {self.author}"
book = Book("Deep Work", "Cal Newport")
print(book)

# Q2 — __add__
class Wallet:
    def __init__(self, money):
        self.money = money
    def __add__(self, other):
        return self.money + other.money
w1 = Wallet(50)
w2 = Wallet(100)
print(w1 + w2)

# Q3 — __eq__
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def __eq__(self, other):
        return self.name == other.name and self.author == other.author
book1 = Book("Deep Work", "Cal Newport")
book2 = Book("Deep Work", "Cal Newport")
print(book1 == book2)

# Q4 — __len__
class Library:
    def __init__(self, books):
        self.books = books
    def __len__(self):
        return len(self.books)
library = Library(["Deep Work", "Atomic Habits", "Clean Code"])
print(len(library))

# Q5 — __getitem__
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    def __getitem__(self, index):
        return self.songs[index]
playlist = Playlist(["Believer", "Faded", "Alone"])
print(playlist[1])

# Q6 — __call__
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, number):
        return self.factor * number
m = Multiplier(5)
print(m(10))

# Q7 — __lt__ & __gt__
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return f"{self.name} -> {self.marks}"
    def __eq__(self, other):
        return self.marks == other.marks
    def __lt__(self, other):
        return self.marks < other.marks
student1 = Student("Banku", 85)
student2 = Student("Gunjan", 85)
print(student1)
print(student1 == student2)
print(student1 < student2)