class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        start = 0
        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                swap = nums[start]

                nums[start] = nums[i]
                nums[i] = swap
                start += 1

        return nums