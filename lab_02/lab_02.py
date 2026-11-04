import csv
from sys import argv

def add_logic(student_list, name, phone, age, email):
    new_item = {"name": name, "phone": phone, "age": age, "email": email}
    insertPosition = 0
    for item in student_list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    student_list.insert(insertPosition, new_item)
    return insertPosition

def delete_logic(student_list, name):
    deletePosition = -1
    for item in student_list:
        if name == item["name"]:
            deletePosition = student_list.index(item)
            break
    if deletePosition != -1:
        del student_list[deletePosition]
    return deletePosition

def update_logic(student_list, old_name, new_name, new_phone, new_age, new_email):
    pos = delete_logic(student_list, old_name)
    if pos == -1:
        return False
    add_logic(student_list, new_name, new_phone, new_age, new_email)
    return True

def find_student(student_list, name):
    for item in student_list:
        if name == item["name"]:
            return item
    return None

def load_data(file_name):
    student_list = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_list.append(row)
    except FileNotFoundError:
        pass 
    return student_list

def save_data(file_name, student_list):
    with open(file_name, "w", newline='', encoding="utf-8") as csvfile:
        fieldnames = ["name", "phone", "age", "email"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in student_list:
            writer.writerow(student)

def printAlllList(student_list):
    for elem in student_list:
        strForPrint = f"Student name is {elem['name']}, Phone is {elem['phone']}, Age is {elem['age']}, Email is {elem['email']}"
        print(strForPrint)

def AddNewElement(student_list):
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    email = input("Please enter student email: ")
    add_logic(student_list, name, phone, age, email)
    print("New element has been added")

def DeleteElement(student_list):
    name = input("Please enter name to be deleted: ")
    deletePosition = delete_logic(student_list, name)
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))

def UpdateElement(student_list):
    name = input("Please enter name to be updated: ")
    current_item = find_student(student_list, name)

    if not current_item:
        print("Element was not found")
    else:
        print("Enter new data for the student (leave blank to keep current value):")
        new_name = input(f"Please enter new name [{current_item['name']}]: ") or current_item['name']
        new_phone = input(f"Please enter new phone [{current_item['phone']}]: ") or current_item['phone']
        new_age = input(f"Please enter new age [{current_item['age']}]: ") or current_item['age']
        new_email = input(f"Please enter new email [{current_item['email']}]: ") or current_item['email']

        update_logic(student_list, new_name, new_phone, new_age, new_email)
        print("Element has been updated successfully")

def main():
    if len(argv) < 2:
        print("Помилка: вкажіть файл для роботи. Приклад: python3 lab_02.py lab_02.csv")
        return
    file_name = argv[1]
    student_list = load_data(file_name)

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                AddNewElement(student_list)
                printAlllList(student_list)
            case "U" | "u":
                print("Existing element will be updated")
                UpdateElement(student_list)
                printAlllList(student_list)
            case "D" | "d":
                print("Element will be deleted")
                DeleteElement(student_list)
                printAlllList(student_list)
            case "P" | "p":
                print("List will be printed")
                printAlllList(student_list)
            case "X" | "x":
                print("Exit()")
                save_data(file_name, student_list) 
                break
            case _:
                print("Wrong chouse")

if __name__ == "__main__":
    main()