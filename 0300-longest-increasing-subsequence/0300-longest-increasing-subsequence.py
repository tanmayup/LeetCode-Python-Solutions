class Solution:
    def rec(self, prev, i, nums, dp):
        if i == len(nums):
            return 0

        if dp[i][prev+1] != -1:
            return dp[i][prev+1]

        take = 0
        if prev == -1 or nums[prev] < nums[i]:
            take = 1 + self.rec(i, i+1, nums, dp)
        not_take = self.rec(prev, i+1, nums, dp)

        dp[i][prev+1] = max(take, not_take)

        return dp[i][prev+1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for _ in range(n+1)] for _ in range(n)]
        return self.rec(-1, 0, nums, dp)