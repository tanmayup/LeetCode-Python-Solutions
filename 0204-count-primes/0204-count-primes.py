class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        l = [True] * n
        l[0], l[1] = False, False
        count = n-2

        for i in range(2, int(n ** 0.5)+1):
            if l[i]:
                mul = i
                while i * mul < n:
                    if l[i*mul]:
                        count -= 1
                    l[i*mul] = False
                    mul += 1


        return count