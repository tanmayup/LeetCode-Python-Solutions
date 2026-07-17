class Solution:
    # def rec(self, i, nums, dp):
    #     if i >= len(nums):
    #         return 0

    #     if dp[i] != -1:
    #         return dp[i]

    #     take = nums[i] + self.rec(i+2, nums, dp)
    #     not_take = self.rec(i+1, nums, dp)
        
    #     if dp[i] == -1:
    #         dp[i] = max(take, not_take)

    #     return dp[i]

    def rob(self, nums: List[int]) -> int:
        # dp = [-1] * len(nums)
        # return self.rec(0, nums, dp)
        # ==========================================
        # dp = [-1] * (len(nums) + 2)
        # dp[-1], dp[-2] = 0, 0

        # for i in range(len(nums)-1, -1, -1):
        #     dp[i] = max(nums[i]+dp[i+2], dp[i+1])

        # return dp[0]
        # ==========================================
        a, b = 0, 0
        for i in range(len(nums)-1, -1, -1):
            c = max(nums[i]+b, a)
            a, b = c, a

        return c