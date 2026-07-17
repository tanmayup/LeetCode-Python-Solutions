class Solution(object):
    def twoSum(self, nums, target):
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] == target - nums[i]:
        #             return [i, j]

        dict1 = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in dict1:
                return [dict1[rem], i]

            dict1[nums[i]] = i