# Q1 — Safe Division
import logging
logging.basicConfig(level = logging.INFO)
logging.info("Program started")
try:
    a = int(input())
    b = int(input())
    logging.info("User input received")
    c = a/b
    logging.info("Division successful")
    print(c)
except ZeroDivisionError:
    logging.error("Division by Zero")
except ValueError:
    logging.error("Invalid input")
logging.info("Program ended")

# Q2 — Login System
logging.info("Program started")
correct_password = "python123"
password = input()
if password == correct_password:
    print("Login Successful")
    logging.info("User Logged in Successfully")
else:
    print("Invalid Password")
    logging.warning("Incorrect Password Entered")
logging.info("Program ended")

# Q3 — File Opening
try:
    file = open("data.txt", "r")
    logging.info("File Opened Successfully")
except FileNotFoundError:
    print("File does not exist")
    logging.error("File does not exist")