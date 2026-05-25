class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack_mini:
            self.stack_mini.append(val)
        elif val <= self.stack_mini[-1]:
            self.stack_mini.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.stack_mini[-1]:
            self.stack_mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_mini[-1]
