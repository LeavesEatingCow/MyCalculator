class Calculator:
    def __init__(self, operands, operations):
        self.operands = operands
        self.operations = operations

    def __call__(self, *args, **kwargs):
        self.evaluate()

    def add(self):
        num1 = self.operands.pop()
        num2 = self.operands.pop()

        self.operands.append(num1 + num2)

    def sub(self):
        num1 = self.operands.pop()
        num2 = self.operands.pop()

        self.operands.append(num2 - num1)

    def mult(self):
        num1 = self.operands.pop()
        num2 = self.operands.pop()

        self.operands.append(num1 * num2)

    def div(self):
        num1 = self.operands.pop()
        num2 = self.operands.pop()

        if num1 == 0:
            raise ZeroDivisionError()

        self.operands.append(num2 / num1)

    def mod(self):
        num1 = self.operands.pop()
        num2 = self.operands.pop()

        if num1 == 0:
            raise ZeroDivisionError()

        self.operands.append(num2 % num1)

    def evaluate(self):
        while self.operations:
            operation = self.operations.pop()

            if operation == '+':
                self.add()
            if operation == '-':
                self.minus()
            if operation == '*':
                self.mult()
            if operation == '/':
                self.div()
            if operation == '%':
                self.mod()




