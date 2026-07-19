### Student management system ###



students = []
def load_data():
    try:
        file = open("students.txt", "r")
    

        for line in file:
            data = line.strip().split("|")

            if len(data) == 3:
                student = {
                           
                    "id": data[0],
                    "name": data[1],
                    "marks": data[2],
            
                }
                students.append(student)

        file.close()

    except FileNotFoundError:
        pass


def save_data():
    file = open("students.txt", "w")

    for student in students:
        file.write(student["id"] + "," + student["name"] + "," + student["marks"] + "\n")

    file.close()


def add_student():
    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:
            print("Student ID already exists.\n")
            return

    name = input("Enter Student Name: ")
    marks = input("Enter Student Marks: ")

    students.append({
        "id": sid,
        "name": name,
        "marks": marks,
    
    })

    save_data()
    print("Student Added Successfully.\n")


def display_students():
    if students == []:
        print("No Student Records Found.\n")
        return

    print("\nID\tName\t\tMarks")
    print("-" * 35)

    for student in students:
        print(student["id"], "\t", student["name"], "\t\t", student["marks"])

    print()


def search_student():
    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:
            print("\nStudent Details")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print()
            return

    print("Student Not Found.\n")


def update_student():
    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:
            name = input("Enter New Name: ")
            marks = input("Enter New Marks: ")

            if name != "":
                student["name"] = name

            if marks != "":
                student["marks"] = marks

            save_data()
            print("Record Updated.\n")
            return

    print("Student Not Found.\n")


def delete_student():
    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:
            students.remove(student)
            save_data()
            print("Student Deleted.\n")
            return

    print("Student Not Found.\n")


def count_students():
    print("Total Students:", len(students))
    print()


load_data()

while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Count Students")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        count_students()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.\n")