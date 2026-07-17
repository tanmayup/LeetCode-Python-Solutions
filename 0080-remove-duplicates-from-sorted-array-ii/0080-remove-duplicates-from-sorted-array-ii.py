class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        start = 0

        for i in range(1, n):
            if nums[start] != nums[i]:
                start += 1
                nums[start] = nums[i]

            else:
                if nums[:start+1].count(nums[i]) < 2:
                    start += 1
                    nums[start] = nums[i]

        return start+1