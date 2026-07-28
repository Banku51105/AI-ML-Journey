# Q1 — csv writer
import csv

students = [
    ["Name","Age","Marks"],
    ["Rahul",20,85],
    ["Priya",21,91],
    ["Amit",19,78]
]
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

# Q2 — csv dict-reader
with open("students.csv", mode="r") as file:
    reader = csv.DictReader(file)
    header = reader.fieldnames
    name_key = header[0]
    marks_key = header[2]
    for row in reader:
        if int(row[marks_key]) > 80:
            print(row[name_key])

# Q3 — json writer
import json
data = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 60000}
]
with open("employees.json", "w") as file:
    json.dump(data, file, indent = 4)

with open("employees.json", "r") as file:
    data = json.load(file)
new_emp = {"name": "Charlie", "salary": 55000}
data.append(new_emp)
with open("employees.json", "w") as file:
    json.dump(data, file, indent = 4)

# Q4 — Binary
with open("photo.jpg", "rb") as original_file:
    image_data = original_file.read()
with open("photo_backup.jpg", "wb") as backup_file:
    backup_file.write(image_data)