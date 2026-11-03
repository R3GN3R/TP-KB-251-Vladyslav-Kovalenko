class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Студент {self.name}, вік: {self.age}"
student_list = [
    Student("Олег", 20),
    Student("Анна", 18),
    Student("Іван", 22),
    Student("Марія", 19)
]
sorted_students = sorted(student_list, key=lambda student: student.age)
print("Відсортований список студентів (за віком):")
for student in sorted_students:
    print(student)