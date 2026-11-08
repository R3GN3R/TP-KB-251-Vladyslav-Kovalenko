import operator
import re

def get_precedance(op):
    if op == '^':
        return 3
    elif op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    return 0

def infix_to_rpn(expression):
    output = []
    stack = []

    tokens = re.findall(r'\d+\.\d+|\d+|[+/*\-^()]', expression)

    for token in tokens:
        if re.match(r'\d+\.\d+|\d+', token):
            output.append(token) 
            
        elif token == '(':
            stack.append(token)
            
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()

        else:
            while stack and stack[-1] != '(' and get_precedance(stack[-1]) >= get_precedance(token):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())
    return output

def evaluate_rpn(rpn_token):
    stack = []

    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul, 
        '/': operator.truediv,
        '^': operator.pow
    }

    for token in rpn_token:
        if token not in operators:
            stack.append(float(token))
        else:
            right_operand = stack.pop()
            left_operand = stack.pop()

            result = operators[token](left_operand, right_operand)
            stack.append(result)

    return stack[0]

def main():
    print("Калькулятор (Зворотний польський запис")
    expression = input("Введіть математичний вираз (наприклад, 3 + 4 * 2 / (1 - 5) ^ 2): ")

    try:
        rpn = infix_to_rpn(expression)
        rpn_string = " ".join(rpn)
        print(f"Зворотний польський запис (ЗПЗ): {rpn_string}")

        result = evaluate_rpn(rpn)
        print(f"Результат: {result}")

    except Exception as e:
        print(f" Помилка при обчисленні виразу. Перевірте правильність введення. Деталі: {e}")

if __name__ == "__main__":
    main()