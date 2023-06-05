from parser import Parser

txt = input('Enter an expression: ')
parse = Parser(txt)
parse.start_analysis()

print(parse.operands)
