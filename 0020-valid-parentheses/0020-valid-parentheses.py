class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "}": "{", "]": "["}
        st = []
        for char in s:
            if char in list(brackets.values()):
                st.append(char)
            else:
                if st and st[-1] == brackets[char]:
                    st.pop()
                else:
                    return False

        return len(st) == 0