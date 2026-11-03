import os
import operations
from datetime import datetime

def log_action(a, b, operation, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H-$M-%S")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "calc_log.txt")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] Дані: a={a}, b={b} | Операція: '{operation}' | Результат: {result}\n")

while True:
    op = input("Команда (+, -, *, /) або 'exit' для виходу: ")
    
    if op.lower() == 'exit':
        print("Програму завершено.")
        break
        
    if op not in ['+', '-', '*', '/']:
        print("Помилка: невідома операція.")
        continue

    a = operations.get_number("Значення a (або 'exit'): ")
    if a == 'exit': break
    
    b = operations.get_number("Значення b (або 'exit'): ")
    if b == 'exit': break

    result = operations.perform_operation(a, b, op)

    print(f"Результат: {result}")
    log_action(a, b, op, result)