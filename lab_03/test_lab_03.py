from student import Student
from student_list import StudentList

def test_add_student():
    directory = StudentList()
    directory.add_student(Student("Zak", "111", "20", "zak@uni.com"))
    directory.add_student(Student("Bob", "222", "18", "bob@uni.com"))

    assert len(directory.students) == 2
    assert directory.students[0].name == "Bob"
    assert directory.students[1].name == "Zak"

def test_delete_student():
    directory = StudentList()
    directory.add_student(Student("Bob", "111", "19", "bob@uni"))

    pos = directory.delete_student("Bob")
    assert pos == 0
    assert len(directory.students) == 0

    pos_not_found = directory.delete_student("Jon")
    assert pos_not_found == -1
    assert len(directory.students) == 0

def test_update_student():
    directory = StudentList()
    directory.add_student(Student("Zak", "222", "21", "Zakk@uni"))

    result = directory.update_student("Zak", Student("Alex", "333", "19", "alex@uni"))
    assert result == True
    assert len(directory.students) == 1
    assert directory.students[0].name == "Alex"
    assert directory.students[0].phone == "333"