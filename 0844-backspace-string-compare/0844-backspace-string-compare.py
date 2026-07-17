class Solution:
    def text(self, string):
        self.string = string
        stack = []
        for char in string:
            if char != "#":
                stack.append(char)
            else:
                if stack:
                    stack.pop()
        
        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.text(s) == self.text(t)
        