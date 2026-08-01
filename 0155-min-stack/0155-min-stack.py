class MinStack:

    def __init__(self):
        self.st = []
        # self.min = float("inf")

    def push(self, value: int) -> None:
        if not self.st:
            self.st.append((value, value))
        # if value < self.min:
        #     self.min = value
        else:
            self.st.append((value, min(value, self.st[-1][-1])))

    def pop(self) -> None:
        self.st.pop()
        # if not self.st:
        #     self.min = float("inf")
        # else:
        #     self.min = self.getMin()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()