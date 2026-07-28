# Q1 — File Modes
with open("students.txt", "w") as f:
    f.write("Banku\nRahul\nAlice")
with open("students.txt", "r") as f:
    print(f.read())
with open("students.txt", "a") as f:
    f.write("\nGunjan")
with open("students.txt", "r") as f:
    print(f.read())

# Q2 — readline & readlines
with open("students.txt", "r") as f:
    print(f.readline())
    print(f.readline())
with open("students.txt", "r") as f:
    print(f.readlines())

# Q3 — Type of readline & readlines
with open("students.txt") as f:
    x = f.read()
    y = f.readlines()
print(type(x))
print(type(y))

# Q4 — seek & tell
with open("students.txt", "r") as f:
    print(f.tell())
    f.read(5)
    print(f.tell())
    f.seek(0)
    print(f.tell())