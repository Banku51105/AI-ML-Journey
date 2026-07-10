# Q1 — Your First Decorator
def decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper
@decorator
def greet():
    print("Hello")
greet()

# Q2 — Decorator with Arguments
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before Function")
        func(*args, **kwargs)
        print("After Function")
    return wrapper
@decorator
def greet(name):
    print(f"Hello {name}")
greet("Banku")

# Q3 — Return Value
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before Function")
        result = func(*args, **kwargs)
        print("After Function")
        return result
    return wrapper
@decorator
def add(a, b):
    return a + b
print(add(10, 20))

# Q4 — Function Call Counter
def decorator(func):
    def wrapper():
        print("Function Called")
        func()
    return wrapper
@decorator
def greet():
    print("Hello")
greet()
greet()

# Q5 — Execution Time (Real-world)
def decorator(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished...")
    return wrapper
@decorator
def work():
    print("Working...")
work()

# Q6 — Logging Arguments
def decorator(func):
    def wrapper(*args):
        print(f"Arguments: {args}")
        result = func(*args)
        return result
    return wrapper
@decorator
def add(a, b):
    return a + b
print(add(10, 20))

# Q7 — Use @wraps
from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper(*args):
        print(f"Arguments: {args}")
        result = func(*args)
        return result
    return wrapper
@decorator
def add(a, b):
    return a + b
print(add(10, 20))

# Decorator Template
from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Before
        result = func(*args, **kwargs)
        # After
        return result
    return wrapper