class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = []
        for num in nums:
            smaller = []
            for num2 in nums:
                if num2 < num:
                    smaller.append(num2)
            count.append(len(smaller))

        return count