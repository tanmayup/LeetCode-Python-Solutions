class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        elif sum(nums) == target:
            return len(nums)

        count = float("inf")
        i, j = 0, 0
        sm = nums[i]
        while j < len(nums):
            if sm >= target:
                count = min(count, j-i+1)
                sm -= nums[i]
                i += 1
            
            else:
                j += 1
                if j < len(nums):
                    sm += nums[j]

        return count