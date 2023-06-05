import re
from collections import deque


class Parser:
    curr_char = 0
    token = ''

    def __init__(self, user_input):
        self.input = user_input
        self.operands = deque()
        self.operations = deque()

    def __call__(self, *args, **kwargs):
        self.start_analysis()

    def start_analysis(self):
        while self.curr_char < len(self.input):
            self.lex()
            self.curr_char += 1

    def lex(self):
        if self.input[self.curr_char].isnumeric() or self.input[self.curr_char] == '+' \
                or self.input[self.curr_char] == '-':
            self.tokenize_num()
            self.token = ''
        else:
            self.lookup()

    def tokenize_num(self):
        num_regex = '[+-]?\d*[.]?\d*'
        self.token += self.input[self.curr_char]
        window_start = self.curr_char
        self.curr_char += 1

        while self.curr_char < len(self.input):
            if re.fullmatch(num_regex, self.input[window_start:self.curr_char + 1]) is None:
                break
            self.token += self.input[self.curr_char]
            self.curr_char += 1

        if self.token == '+' or self.token == '-':
            self.operations.append(self.token)
        else:
            if self.isint(self.token):
                self.operands.append(int(self.token))
            else:
                self.operands.append(float(self.token))

        if self.curr_char < len(self.input):
            self.lookup()

    def lookup(self):
        operations = ['(', ')', '+', '-', '*', '/', '%', ' ']
        operation = self.input[self.curr_char]

        if operation not in operations:
            raise ValueError(operation + ' is not a valid operation')
        else:
            if operation != ' ':
                self.operations.append(operation)

    def isint(self, num):
        try:
            int(num)
            return True
        except ValueError:
            return False
