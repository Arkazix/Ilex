from tokens import TokenType, Token
from typing import Union
from stack import Stack


def is_operator(token: Token):
    return token.type in [TokenType.PLUS, TokenType.MINUS,
                          TokenType.MULTIPLY, TokenType.DIVIDE]


class Parser:

    def __init__(self, stack: Stack) -> None:
        self.stack = stack
        self.suffix_stack = Stack()
        self.op_stack = Stack()

    def read_operator(self) -> None:
        pass

    def infix_to_suffix(self) -> Union[Stack, None]:
        while not self.stack.is_empty():
            infix_stack_top = self.stack.pop_()
            if infix_stack_top == None:
                return
            if infix_stack_top.type == TokenType.NUMBER:
                self.suffix_stack.push(infix_stack_top)
            if is_operator(infix_stack_top):
                self.read_operator()

        return self.suffix_stack
