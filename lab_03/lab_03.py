from sys import argv
from student import Student
from student_list import StudentList
from file_manager import FileManager

def print_all(directory: StudentList):
    for elem in directory.students:
        print(f"Student name is {elem.name}, Phone is {elem.phone}, Age is {elem.age}, Email is {elem.email}")

def main():
    if len(argv) < 2:
        print("Помилка: вкажіть файл для роботи. Приклад: python3 lab_03.py lab_03.csv")
        return

    file_name = argv[1]

    directory = StudentList()
    FileManager.load_data(file_name, directory)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ")
        match choice.upper():
            case "C":
                print("New element will be created: ")
                name = input("Please enter student name: ")
                phone = input("Please enter student phone: ")
                age = input("Please enter student age: ")
                email = input("Please enter student email: ")

                new_student = Student(name, phone, age, email)
                directory.add_student(new_student)
                print("New element has been added")
                print_all(directory)

            case "D":
                print("Element will be deleted")
                name = input("Please enter name to be deleted: ")
                pos = directory.delete_student(name)
                if pos == -1:
                    print("Element was not found")
                else:
                    print (f"Delete position {pos}")
                print_all(directory)

            case "U":
                print("Existing element will be updated")
                name = input("Please enter name to be updated: ")
                current_item = directory.find_student(name)

                if not current_item:
                    print("Element was not found")
                else:
                    print("Enter new data for the student (leave blank to keep current value):")
                    new_name = input("Please enter new name [{current_item.name}]:  ") or current_item.name
                    new_phone = input("Please enter new phone [{current_item.phone}]:  ") or current_item.phone
                    new_age = input("Please enter new age [{current_item.age}]:  ") or current_item.age
                    new_email = input("Please enter new email [{current_item.email}]:  ") or current_item.email

                    update_student = Student(new_name, new_phone, new_age, new_email)
                    directory.update_student(name, update_student)
                    print("Element was updated successfully")
                print_all(directory)

            case "P":
                print("List will be printed:")
                print_all(directory)

            case "X":
                print("Exit()")
                FileManager.save_data(file_name, directory)
                break
            case "-":
                print("Wrong choice")

if __name__ == "__main__":
    main()