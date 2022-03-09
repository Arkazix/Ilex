from src.lexer import Lexer
from src.parser_ import Parser
from src.interpreter import Interpreter


def read_line(line: str, idx: int) -> None:
    lexer = Lexer(line)
    stack_token = lexer.generate_token()
    if stack_token == None:
        return
    stack_token.inverse()

    parser = Parser(stack_token)
    stack_suffixe = parser.infix_to_suffix()
    if stack_suffixe == None:
        return

    stack_suffixe.inverse()
    interpreter = Interpreter(stack_suffixe)
    value = interpreter.evaluate()
    if value == None:
        return
    print(f"{idx}: {value}")
