
class Calculator:

    def __init__(self, operator, num2, num1):
        self.operator = operator
        self.num2 = num2
        self.num1 = num1
        if operator == '+':
            print(num1 + num2)
        elif operator == '-':
            print(num1 - num2)
        elif operator == '/':
            print(num1 / num2)
        elif operator == '*':
            print(num1 * num2)


if __name__ == '__main__':
    print(Calculator.__init__(Calculator, '+', 8, 9))
