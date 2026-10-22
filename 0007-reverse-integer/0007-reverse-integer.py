class Solution:
    def reverse(self, x: int) -> int:
        # ans = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        # return ans if (-1) * (2**31) <= ans <= 2**31-1 else 0

        mul = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        ans = 0
        while x != 0:
            ldig = x % 10
            x //= 10
            ans = ans * 10 + ldig
        
        return ans*sign if -2**31 <= ans <= 2**31-1 else 0