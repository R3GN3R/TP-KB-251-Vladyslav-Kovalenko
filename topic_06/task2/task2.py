import csv
import os

student = [
    {"ім'я": "Олег", "оцінка": 85},
    {"ім'я": "Анна", "оцінка": 95},
    {"ім'я": "Іван", "оцінка": 75},
    {"ім'я": "Марія", "оцінка": 90}
]

sorted_by_grades = sorted(student, key=lambda item: item["оцінка"])

current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir, "student_sorted.csv")

print("Сортування за оцінкою:")
for student in sorted_by_grades:
    print(student)

with open(file_path, "w", encoding="utf-8", newline="") as file:
    fieldnames = ["ім'я", "оцінка"]
    writen = csv.DictWriter(file, fieldnames=fieldnames)

    writen.writeheader()
    writen.writerows(sorted_by_grades)

print("\nДані успішно збережено у файл 'students_sorted.csv'\n")