class Solution:
    def isPalindrome(self, x: int) -> bool:
        xl = list(str(x))
        xlc = []

        for i in range(len(xl)):
            xlc.append(xl[len(xl) - i - 1])

        verdict = None

        for i in range(len(xl)):
            if xl[i] == xlc[i]:
                verdict = True
            else:
                verdict = False
                break

        return verdict