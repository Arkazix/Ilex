from lexer import Lexer
from parser_ import Parser


def read_line(line: str, idx: int) -> None:
    lexer = Lexer(line)
    stack = lexer.generate_token()
    if stack == None:
        return
    stack.inverse()
    parser = Parser(stack)
    suffixe = parser.infix_to_suffix()
    print(suffixe)
    if suffixe == None:
        return
