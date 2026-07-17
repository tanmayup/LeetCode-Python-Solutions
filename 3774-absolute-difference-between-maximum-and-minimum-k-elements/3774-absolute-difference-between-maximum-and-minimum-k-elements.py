class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = nums[0:k]
        high = nums[-k:]

        return abs(sum(high) - sum(low))