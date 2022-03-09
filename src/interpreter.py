from src.tokens import TokenType, Token
from typing import Union, List 
from math import factorial
from src.stack import Stack



def is_operator(token: Token):
    return token.type in [TokenType.PLUS, TokenType.MINUS,
                          TokenType.MULTIPLY, TokenType.DIVIDE,
                          TokenType.POWER, TokenType.FACTORIAL]


def raise_error(prompt: str) -> None:
    raise Exception(prompt)


class Interpreter:

    def __init__(self, suffixe_stack: Stack) -> None:
        self.suffixe_stack = suffixe_stack
        self.stack_value = Stack()

    def evaluate(self) -> Union[int, None]:
        while not self.suffixe_stack.is_empty():
            suffixe_stack_token = self.suffixe_stack.pop_()
            if suffixe_stack_token == None:
                return None
            elif suffixe_stack_token.type == TokenType.NUMBER:
                self.stack_value.push(suffixe_stack_token)
            elif is_operator(suffixe_stack_token):
                func_name = "token_" + \
                    str(suffixe_stack_token.type).split(".")[1].lower()
                eval("self." + func_name + "()")
        
        top_value = self.stack_value.pop_()
        if self.stack_value.get_len() != 0 or top_value == None or top_value.type != TokenType.NUMBER:
            return None
        return top_value.value

    def get_token(self, n: int) -> Union[List[Token], None]:
        token_list: List[Token] = []
        for _ in range(n):
            token = self.stack_value.pop_()
            if token == None or token.value == None:
                return None
            token_list.append(token)
        return token_list

    def token_plus(self) -> None:
        tokens = self.get_token(2)
        if tokens == None:
            raise_error("Not enough argument for adding")
            return
        self.stack_value.push(
            Token(TokenType.NUMBER, value=(tokens[0].value + tokens[1].value))
        )

    def token_minus(self) -> None:
        tokens = self.get_token(2)
        if tokens == None:
            raise_error("Not enough argument for substracting")
            return
        self.stack_value.push(
            Token(TokenType.NUMBER, value=(tokens[1].value - tokens[0].value))
        )

    def token_divide(self) -> None:
        tokens = self.get_token(2)
        if tokens == None or tokens[0].value == 0:
            raise_error("Error while divide")
            return
        self.stack_value.push(
            Token(TokenType.NUMBER, value=(tokens[1].value / tokens[0].value))
        )

    def token_multiply(self) -> None:
        tokens = self.get_token(2)
        if tokens == None:
            raise_error("Not enough argument for multiply")
            return
        self.stack_value.push(
            Token(TokenType.NUMBER, value=(tokens[0].value * tokens[1].value))
        )

    def token_power(self) -> None:
        tokens = self.get_token(2)
        if tokens == None:
            raise_error("Not enough argument for power")
            return
        self.stack_value.push(
            Token(TokenType.NUMBER, value=(tokens[1].value ** tokens[0].value))
        )

    def token_factorial(self) -> None:
        tokens = self.get_token(1)
        if tokens == None:
            raise_error("Not enough argument for power")
            return
        self.stack_value.push(
            Token(TokenType.NUMBER, value=(factorial(tokens[0].value)))
        )
