def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль"
    return a / b

def calculator_match(a, b, operation):
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

while True:
    operation = input("Команда (+, -, *, /) або 'exit' для виходу: ")
    if operation.lower() == 'exit':
        print("Програму завершено.")
        break
    if operation not in ['+', '-', '/', '*']:
        print("Помилка: невідома операція. Спробуйте ще раз.")
        continue
    try: 
        a = float(input("Значення a: "))
        b = float(input("Значення b: "))
    except ValueError:
        print("Помилка: введено не число. Спробуйте ще раз.")
        continue
    print("Результат match:", calculator_match(a, b, operation))