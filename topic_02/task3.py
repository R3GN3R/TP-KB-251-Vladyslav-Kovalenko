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

a = float(input("Значення a: "))
b = float(input("Значення b: "))
operation = input("Команда: ")

print("Результат match:", calculator_match(a, b, operation))