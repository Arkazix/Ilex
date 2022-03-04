from typing import List
import re


class Lexer:
    def __init__(self) -> None:
        self.tokens = (
            'NUMBER', 'PLUS', 'MINUS', 'TIMES',
            'DIVIDE', 'LPAREN', 'RPAREN'
        )

    def lex(self, line: str) -> List:
        pass


class Parser:

    def __init__(self) -> None:
        pass

    def parse(self, token_list: List) -> int:
        pass


if __name__ == '__main__':
    lexer = Lexer()
    parser = Parser()
    while True:
        line = input("> ")
        if line == "exit()":
            break
        token_list = lexer.lex(line)
        print(parser.parse(token_list))
