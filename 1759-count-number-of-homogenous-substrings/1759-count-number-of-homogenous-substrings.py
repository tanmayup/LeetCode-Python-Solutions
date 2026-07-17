class Solution:
    def countHomogenous(self, s: str) -> int:
        subs = []
        count = 1
        num = 0
        for i in range(len(s)):
            if i != len(s)-1 and s[i] == s[i+1]:
                count += 1

            else:
                num += int(count * (count + 1) / 2)
                count = 1

        return num % (10**9 + 7)