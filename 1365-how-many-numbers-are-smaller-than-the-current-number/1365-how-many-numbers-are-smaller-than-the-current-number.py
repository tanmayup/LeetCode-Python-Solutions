class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # ans = []
        # for num in nums:
        #     count = 0
        #     for num2 in nums:
        #         if num2 < num:
        #             count += 1
        #     ans.append(count)

        # return ans

        numsc = []
        numsc[:] = nums[:]

        nums.sort(reverse=True)
        count = {}
        i = 0
        l = len(nums)

        while i != len(nums)-1:
            if nums[i] != nums[i+1]:
                count[nums[i]] = l - i - 1
            i += 1
        count[nums[-1]] = 0

        ans = []
        for num in numsc:
            ans.append(count[num])

        return ans