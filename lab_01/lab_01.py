list = [
    {"name":"Bob", "phone":"0631234567", "age":"20", "email":"bob@university.edu"},
    {"name":"Emma", "phone":"0631234567", "age":"19", "email":"emma@university.edu"},
    {"name":"Jon",  "phone":"0631234567", "age":"21", "email":"jon@university.edu"},
    {"name":"Zak",  "phone":"0631234567", "age":"18", "email":"zak@university.edu"}
]
def printAllList():
    for elem in list:
        strForPrint = f"Student name is {elem['name']}, Phone is {elem['phone']}, Age is {elem['age']}, Email is {elem['email']}"
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    email = input("Please enter student email: ")
    newItem = {"name": name, "phone": phone, "age": age, "email": email}

    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        del list[deletePosition]
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1
    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break
    if updatePosition == -1:
        print("Element was not found")
    else:
        print("Enter new data for the student (leave blank to keep current value):")
        current_item = list[updatePosition]
        new_name = input(f"Please enter new name [{current_item['name']}]: ") or current_item['name']
        new_phone = input(f"Please enter new phone [{current_item['phone']}]: ") or current_item['phone']
        new_age = input(f"Please enter new age [{current_item['age']}]: ") or current_item['age']
        new_email = input(f"Please enter new email [{current_item['email']}]: ") or current_item['email']

        del list[updatePosition]
        newItem = {"name": new_name, "phone": new_phone, "age": new_age, "email": new_email}

        insertPosition = 0
        for item in list:
            if new_name > item["name"]:
                insertPosition += 1
            else:
                break
        list.insert(insertPosition, newItem)
        print("Element has been updated successfully")
    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")

main()