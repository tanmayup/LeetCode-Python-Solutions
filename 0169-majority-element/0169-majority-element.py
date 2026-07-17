class Solution(object):
    def majorityElement(self, nums):
        nums2 = list(set(nums))
        for el in nums2:
            if nums.count(el) > (len(nums) / 2):
                return el