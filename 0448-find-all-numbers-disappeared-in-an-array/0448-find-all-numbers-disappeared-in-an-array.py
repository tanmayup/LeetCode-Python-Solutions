class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        full = set([num for num in range(1, len(nums)+1)])
        nums = set(nums)

        return list(full-nums)