class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        l = [True] * n
        l[0], l[1] = False, False
        count = n-2

        for i in range(2, int(n ** 0.5)+1):
            if l[i]:
                for j in range(i*i, n, i):
                    if l[j]:
                        count -= 1
                        l[j] = False


        return count