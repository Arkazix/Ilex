class Stack:

    def __init__(self) -> None:
        self.stack = []

    def push(self, token):
        self.stack.append(token)

    def pop_(self):
        if self.stack:
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
