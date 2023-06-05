import re


class Parser:
    curr_char = 0
    token = ''

    def __init__(self, user_input):
        self.input = user_input
        self.operands = list()
        self.operations = list()

    def start_analysis(self):
        while self.curr_char < len(self.input):
            self.lex()

    def lex(self):
        if self.input[self.curr_char].isnumeric() or self.input[self.curr_char] == '+' or self.input[self.curr_char] == '-':
            self.tokenize_num()
            self.token = ''

    def tokenize_num(self):
        int_regex = '[+-]?\d*'
        float_regex = '[+-]?\d*.\d*'
        self.token += self.input[self.curr_char]
        window_start = self.curr_char
        self.curr_char += 1

        is_int = re.match(int_regex, self.input[window_start:self.curr_char]).group() != re.match(int_regex, self.input[window_start:self.curr_char]).string
        is_float = re.match(float_regex, self.input[window_start:self.curr_char]).group() != re.match(float_regex, self.input[window_start:self.curr_char]).string

        while self.curr_char < len(self.input):
            if not(is_int or is_float):
                break
            self.token += self.input[self.curr_char]
            self.curr_char += 1

        if is_float:
            self.token = float(self.token)
            print('is float')
        if is_int:
            self.token = int(self.token)
            print('is int')

        print(self.token)

        self.operands.append(self.token)
