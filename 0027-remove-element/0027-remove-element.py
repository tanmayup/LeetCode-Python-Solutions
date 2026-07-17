class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)

        while val in nums:
            nums.remove(val)
        length = len(nums)
        print(nums, length)