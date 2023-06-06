from parser import Parser
from calculator import Calculator

txt = input('Enter an expression: ')
parse = Parser(txt)
parse()


calc = Calculator(parse.operands, parse.operations)
calc()

print(calc.operands.pop())
