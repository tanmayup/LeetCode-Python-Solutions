class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1 or n == 2:
        #     return n

        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        ways = [0] * (n+1)

        ways[0], ways[1] = 1, 2

        for i in range(2, n):
            ways[i] = ways[i-1] + ways[i-2]

        return ways[-2]