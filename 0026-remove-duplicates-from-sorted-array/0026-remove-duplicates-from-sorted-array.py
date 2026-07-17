class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # rem = []
        # i = 0
        # while i != len(nums):
        #     if nums.count(nums[i]) == 1:
        #         rem.append(nums[i])
        #         i += 1
            
        #     elif nums.count(nums[i]) > 1:
        #         rem.append(nums[i])
        #         i += nums.count(nums[i])

        # nums[:] = rem[:]

        # return len(nums)

        n = len(nums)
        start = 0

        for i in range(1, n):
            if nums[start] != nums[i]:
                start += 1
                nums[start] = nums[i]

        return start + 1