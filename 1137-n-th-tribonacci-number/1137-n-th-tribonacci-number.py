class Solution:
    def tribonacci(self, n: int) -> int:
        initials = [0, 1, 1]
        if n == 0 or n == 1 or n == 2:
            return initials[n]

        else:
            for _ in range(n-2):
                initials.append(initials[-1] + initials[-2] + initials[-3])

        return initials[-1]