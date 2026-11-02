def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try: 
        return a / b
    except ZeroDivisionError:
        return "Помилка, ділення на 0"

def calculator_extent(a, b, operation):
    match operation:
        case '+':
            return add(a, b)
        case '-':
            return subtract(a, b)
        case '*':
            return multiply(a, b)
        case '/':
            return divide(a, b)
        case _:
            return "Помилка: невідома операція"

def get_number(promt):
    while True:
        user_input = input(promt)
        if user_input.lower() == 'exit':
            return 'exit'
        try:
            return float(user_input)
        except ValueError:
            print("Помилка: введено не число. Спробуйте ще раз.")

while True:
    operation = input("Команда (+, -, *, /) або 'exit' для виходу: ")

    if operation.lower() == 'exit':
        print("Програму завершено.")
        break

    if operation not in ['+', '-', '*', '/']:
        print("Помилка: невідома операція.")
        continue

    a = get_number("Значення a (або 'exit'): ")
    if a == 'exit': break
    b = get_number("Значення b (або 'exit'): ")
    if b == 'exit': break


    print("Результат match:", calculator_extent(a, b, operation))