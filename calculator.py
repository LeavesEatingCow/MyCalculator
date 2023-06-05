from collections import deque


class Calculator:
    def __init__(self):
        self.operands = deque()
        self.operations = deque()
