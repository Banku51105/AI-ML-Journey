# Practice Set 1 — Basic Exception Handling
# Q1 — Safe List Access
try:
    numbers = [10, 20, 30]
    index = int(input())
    print(numbers[index])
except IndexError as e:
    print(e)
except ValueError:
    print("Invalid input")
finally:
    print("Program Ended")

# Q2 — Safe Dictionary Lookup
try:
    student = {"name": "Banku", "age": 20}
    key = input()
except KeyError:
    print("Key not found")
else:
    print(student[key])

# Q3 — Multiple Exceptions
try:
    a = int(input())
    b = int(input())
    c = a/b
    # print(c)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {c}")
finally:
    print("Program Finished")

# Practice Set 2 — Different Exceptions + raise
# Q1 — Age Validation (raise)
try:
    age = int(input())
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 120:
        raise ValueError("Invalid human age")
    else:
        print("Valid age")
except ValueError as e:
    print(e)

# Q2 — Shopping Cart
try:
    cart = {
    "apple": 40,
    "banana": 20,
    "milk": 60
    }
    item = input()
    print(cart[item])
except KeyError:
    print("Item not available")

# Q3 — Calculator with Operator Validation (raise)
try:
    a = int(input())
    op = input()
    b = int(input())
    if op not in ["+","-","*","/"]:
        raise ValueError("Unsupported operator")
    else:
        if op == "+":
            print(a+b)
        elif op == "-":
            print(a-b)
        elif op == "*":
            print(a*b)
        elif op == "/":
            print(a/b)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

# Practice Set 3 — Custom Exceptions
# Q1 — Create Your First Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, msg):
        self.msg = msg
def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age Cannot Be Negative")
    else:
        print("Valid Age")

# Q2 — Bank Withdrawal
class InsufficientBalanceError(Exception):
    def __init__(self, msg):
        self.msg = msg
balance = 5000
def withdraw(amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient Balance")
    else:
        print("Withdrawal Successful")
        print(f"Remaining Balance: {balance-amount}")

# Q3 — Login System
class InvalidPasswordError(Exception):
    def __init__(self, msg):
        self.msg = msg
correct_password = "python123"
def login(password):
    if password != correct_password:
        raise InvalidPasswordError("Incorrect Password")
    else:
        print("Login Successful")

# Q4 — Student Marks
class InvalidMarksError(Exception):
    def __init__(self, msg):
        self.msg = msg
def input_marks(marks):
    if marks < 0:
        raise InvalidMarksError("Marks cannot be negative")
    elif marks > 100:
        raise InvalidMarksError("Marks cannot be more than 100")
    else:
        print("Marks Accepted")