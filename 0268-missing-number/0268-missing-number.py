class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # full = [num for num in range(n+1)]

        # ans = 0
        # nums.extend(full)
        # for el in nums:
        #     ans ^= el

        # return ans

        return sum([num for num in range(len(nums)+1)]) - sum(nums)