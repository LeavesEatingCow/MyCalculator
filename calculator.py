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

        try:
            self.operands.append(num2 / num1)
        except ZeroDivisionError:
            print('Can\'t divide by 0!')

    def mod(self):
        num1 = self.operands.pop()
        num2 = self.operands.pop()

        try:
            self.operands.append(num2 % num1)
        except ZeroDivisionError:
            print('Can\'t divide by 0!')

    def evaluate(self):
        order_of_op1 = {'*': self.mult, '/': self.div, '%': self.mod}
        order_of_op2 = {'+': self.add, '-': self.sub}

        while self.operations:
            operation = self.operations.pop()

            if operation in order_of_op1:
                order_of_op1.get(operation)()
            elif operation in order_of_op2:
                order_of_op2.get(operation)()





