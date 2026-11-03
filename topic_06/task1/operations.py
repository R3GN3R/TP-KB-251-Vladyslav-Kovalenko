import functions

def get_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'exit':
            return 'exit'
        try:
            return float(user_input)
        except ValueError:
            print("Помилка: введено не число. Спробуйте ще раз.")

def perform_operation(a, b, operation):
    match operation:
        case '+':
            return functions.add(a, b)
        case '-':
            return functions.subtract(a, b)
        case '*':
            return functions.multiply(a, b)
        case '/':
            return functions.divide(a, b)
        case _:
            return "Помилка: невідома операція"