def add_student(students, name, marks):
    if name not in students:
        students[name] = marks
        return True
    else:
        return "Student already exists"
def delete_student(students, name):
    if name in students:
        students.pop(name)
        return True
    else:
        return "Student does not exist"
def update_student(students, name, marks):
    if name in students:
        students[name] = marks
        return True
    else:
        return "Student does not exist"
def search_student(students, name):
    if name in students:
        return students[name]
    else:
        return "Student does not exist"
def show_all_students(students):
    return students
def main():
    students = {}

    while True:
        print("1: Add Student Marks")
        print("2: Delete Student Marks")
        print("3: Update Student Marks")
        print("4: Search Student Marks")
        print("5: List Of All Students")
        print("6: Exit\n")

        choice = int(input())
        if choice == 1:
            name = input("Enter name:")
            marks = int(input("Enter marks: "))
            result = add_student(students, name, marks)
            if result is True:
                print("Student Added Successfully")
            else:
                print(result)
        elif choice == 2:
            name = input("Enter name:")
            result = delete_student(students, name)
            if result is True:
                print("Student Deleted Successfully")
            else:
                print(result)
        elif choice == 3:
            name = input("Enter name:")
            marks = int(input("Enter marks: "))
            result = update_student(students, name, marks)
            if result is True:
                print("Student Updated Successfully")
            else:
                print(result)
        elif choice == 4:
            name = input("Enter name:")
            result = search_student(students, name)
            if result != "Student does not exist":
                print(f"{name} -> {result}")
            else:
                print(result)
        elif choice == 5:
            all_students = show_all_students(students)
            if not all_students:
                print("No students found")
            for name, marks in all_students.items():
                print(f"{name} -> {marks}")
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
main()