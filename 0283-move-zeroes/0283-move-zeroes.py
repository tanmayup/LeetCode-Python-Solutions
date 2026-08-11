class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = 0
        # l = len(nums)
        # while l:
        #     if nums[n] == 0:
        #         nums.append(0)
        #         nums.pop(n)

        #     else:
        #         n += 1
        #     l -= 1

        n = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[n], nums[i] = nums[i], nums[n]
                n += 1