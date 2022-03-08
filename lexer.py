from tokens import Token, TokenType
from typing import Union
from stack import Stack


DIGITS = "0123456789"
WHITESPACE = " \t\n\r\v\f"
ASSOCIATIVITY_LEFT = 0
ASSOCIATIVITY_RIGHT = 1


def raise_error(prompt: str) -> None:
    raise Exception(prompt)


class Lexer:

    def __init__(self, line: str) -> None:
        self.chars = iter(line)
        self.current_char = ""
        self.advance()

    def advance(self) -> Union[str, None]:
        try:
            self.current_char = next(self.chars)
        except StopIteration:
            self.current_char = None

    def generate_number(self) -> Union[Token, None]:
        number = ""
        while self.current_char != None and self.current_char in DIGITS:
            number = number + self.current_char
            self.advance()
        try:
            return Token(TokenType.NUMBER, None, None, int(number))
        except ValueError:
            raise_error(f"Bad value for int: " + number)

    def generate_token(self) -> Union[Stack, None]:
        stack = Stack()
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
                continue
            elif self.current_char in DIGITS:
                tokenNumber = self.generate_number()
                if tokenNumber == None:
                    return
                stack.push(tokenNumber)
            elif self.current_char == "+":
                self.advance()
                stack.push(Token(TokenType.PLUS, 1, ASSOCIATIVITY_LEFT))
            elif self.current_char == "-":
                self.advance()
                stack.push(Token(TokenType.MINUS, 1, ASSOCIATIVITY_LEFT))
            elif self.current_char == "*":
                self.advance()
                stack.push(Token(TokenType.MULTIPLY, 2, ASSOCIATIVITY_LEFT))
            elif self.current_char == "/":
                self.advance()
                stack.push(Token(TokenType.DIVIDE, 2, ASSOCIATIVITY_LEFT))
            elif self.current_char == "(":
                self.advance()
                stack.push(Token(TokenType.LPAREN, 0))
            elif self.current_char == ")":
                self.advance()
                stack.push(Token(TokenType.RPAREN, 0))
            else:
                raise_error(
                    f"Unknow char: {self.current_char} x{ord(self.current_char)}")
                return None
        return stack
