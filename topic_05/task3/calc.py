import operations
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