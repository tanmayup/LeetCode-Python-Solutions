class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        s *= 2
        string = "".join(s)

        for i in range(n):
            if goal == string[i:i+n]:
                return True

        return False