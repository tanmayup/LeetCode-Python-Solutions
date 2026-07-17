# class Stack:
#     def __init__(self):
#         self.st = []

#     def push(self, x):
#         self.st.append(x)

#     def pop(self):
#         if len(self.st) == 0:
#             return -1

#         x = self.st[-1]
#         self.st.pop()
#         return x
    
#     def top(self):
#         if len(self.st) == 0:
#             return -1
        
#         return self.st[-1]

# class Solution():
#     def isValid(self, s: str) -> bool:
#         st = Stack()
#         pairs = {")":"(",
#                  "]":"[",
#                  "}":"{"}
#         for char in s:
#             if char in pairs.values():
#                 st.push(char)
#             else:
#                 if st.top() == pairs[char]:
#                     st.pop()

#                 else:
#                     return False
                
#         return st.top() == -1

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opens = {'(', '[', '{'}
        pairs = {")":"(", 
        "]":"[", 
        "}":"{"}

        for char in s:
            if char in opens:
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()

        return len(stack) == 0