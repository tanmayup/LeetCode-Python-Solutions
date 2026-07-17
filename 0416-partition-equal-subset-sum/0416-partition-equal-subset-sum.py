class Solution:
    def ks(self, i, w, values, dp):
        if i == len(values):
            return 0

        if dp[i][w] != -1:
            return dp[i][w]

        take = 0
        if w >= values[i]:
            take = values[i] + self.ks(i+1, w-values[i], values, dp)
        not_take = self.ks(i+1, w, values, dp)

        if dp[i][w] == -1:
            dp[i][w] = max(take, not_take)

        return dp[i][w]

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if len(nums) == 1:
            return False

        if total % 2 == 1:
            return False

        dp = [[-1] * (total // 2 + 1) for _ in range(len(nums))]
        return self.ks(0, total // 2, nums, dp) == total // 2