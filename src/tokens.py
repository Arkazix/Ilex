from dataclasses import dataclass
from typing import Any
from enum import Enum


class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6
    POWER = 7
    FACTORIAL = 8


@dataclass
class Token:
    type: TokenType
    priority: Any = None
    associativity: Any = None
    value: Any = None

    def __repr__(self) -> str:
        return f"Type: {self.type} " + \
            ("Value: " + str(self.value) if self.value != None else "") + \
            (" Priority: " + str(self.priority) if self.priority != None else "") + \
            (" associativity: " + str(self.associativity)
             if self.associativity != None else "") + "\n"
