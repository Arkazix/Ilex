from const import ASSOCIATIVITY_LEFT
from tokens import TokenType, Token
from typing import Union
from stack import Stack


def is_operator(token: Token):
    return token.type in [TokenType.PLUS, TokenType.MINUS,
                          TokenType.MULTIPLY, TokenType.DIVIDE]


def raise_error(prompt: str) -> None:
    raise Exception(prompt)


class Parser:

    def __init__(self, stack: Stack) -> None:
        self.stack = stack
        self.suffix_stack = Stack()
        self.op_stack = Stack()

    def read_operator(self, element: Token) -> None:
        if self.op_stack.is_empty():
            self.op_stack.push(element)
            return

        cond: bool = element.associativity == ASSOCIATIVITY_LEFT

        while (current_op := self.op_stack.top_element()) != None and \
                element.priority - cond < current_op.priority:
            self.suffix_stack.push(current_op)
            self.op_stack.pop_()
            current_op = self.op_stack.top_element()

        self.op_stack.push(element)

    def read_parenthesis(self) -> None:
        while (current_op := self.op_stack.top_element()) != None and current_op.type != TokenType.LPAREN:
            self.suffix_stack.push(current_op)
            self.op_stack.pop_()

        if current_op == None:
            raise_error("Error: Unmatch bracket")
        else:
            self.op_stack.pop_()

    def infix_to_suffix(self) -> Union[Stack, None]:
        while not self.stack.is_empty():
            infix_stack_top = self.stack.pop_()
            if infix_stack_top == None:
                return
            elif infix_stack_top.type == TokenType.NUMBER:
                self.suffix_stack.push(infix_stack_top)
            elif is_operator(infix_stack_top):
                self.read_operator(infix_stack_top)
            elif infix_stack_top.type == TokenType.LPAREN:
                self.op_stack.push(infix_stack_top)
            elif infix_stack_top.type == TokenType.RPAREN:
                self.read_parenthesis()

        while not self.op_stack.is_empty():
            op = self.op_stack.pop_()
            if op != None:
                self.suffix_stack.push(op)

        return self.suffix_stack
