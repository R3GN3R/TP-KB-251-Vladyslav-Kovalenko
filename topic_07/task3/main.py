from calc_logic import Calculator
calc = Calculator()
while True:
    operation = input("Команда (+, -, *, /) або 'exit' для виходу: ")
    if operation.lower() == 'exit':
        print("Програму завершено.")
        break
    if operation not in ['+', '-', '*', '/']:
        print("Помилка: невідома операція.")
        continue

    a = Calculator.get_number("Значення a (або 'exit'): ")
    if a == 'exit': break
    b = Calculator.get_number("Значення b (або 'exit'): ")
    if b == 'exit': break

    result = calc.execute_operaton(a, b, operation)

    print(f"Результат: {result}")
    print("-" * 20)