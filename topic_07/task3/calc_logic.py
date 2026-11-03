class Calculator:
    def  add(self, a, b):
        return a + b
    def substact(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Помилка: ділення на нуль"
    def execute_operaton(self, a, b, operation):
        match operation:
            case '+': return self.add(a, b)
            case '-': return self.substact(a, b)
            case '*': return self.multiply(a, b)
            case '/': return self.divide(a, b)
            
    @staticmethod
    
    def get_number(promt):
        while True:
            user_input = input(promt)
            if user_input.lower() == 'exit':
                return 'exit'
            try:
                return float(user_input)
            except ValueError:
                print("Помилка: введено не число. Спробуйте ще раз.")