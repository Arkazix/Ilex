from interpreter import Interpreter
from parser_ import Parser
from lexer import Lexer


def read_line(text: str, line_number: int) -> None:
    try:
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: return
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(f"{line_number + 1}: {value}")
    except Exception as e:
        print(e)