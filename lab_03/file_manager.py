import csv
from student import Student
from student_list import StudentList

class FileManager:
    @staticmethod
    def load_data(file_name, directory: StudentList):
        try:
            with open(file_name, encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(row["name"], row ["phone"], row["age"], row["email"])
                    directory.add_student(student)
        except FileNotFoundError:
            pass

    @staticmethod
    def save_data(file_name, directory: StudentList):
        with open(file_name, "w", newline='', encoding="utf-8") as csvfile:
            fieldname = ["name", "phone", "age", "email"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldname)
            writer.writeheader()
            for student in directory.students:
                writer.writerow({
                    "name": student.name,
                    "phone": student.phone,
                    "age": student.age,
                    "email": student.email
                })