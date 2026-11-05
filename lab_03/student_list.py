from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        insert_position = 0
        for item in self.students:
            if student.name > item.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, student)
        return insert_position

    def delete_student(self, name):
        delete_position = -1
        for item in self.students:
            if name == item.name:
                delete_position = self.students.index(item)
                break
        if delete_position != -1:
            del self.students[delete_position]
        return delete_position

    def update_student(self, old_name, new_student: Student):
        pos = self.delete_student(old_name)
        if pos == -1:
            return False
        self.add_student(new_student)
        return True

    def find_student(self, name):
        for item in self.students:
            if name == self.item:
                return item
        return None