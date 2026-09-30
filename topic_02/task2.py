def add(a, b):
    return a + b

def substact(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка, ділення на 0"
    return a / b
def calc_if_else(a, b, operator):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return substact(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    else:
        return "Помилка невідома операція"

a = float(input("Значення a: "))
b = float(input("Значення b: "))
operator = input("Команда: ")

print("Результат:", calc_if_else(a, b, operator))