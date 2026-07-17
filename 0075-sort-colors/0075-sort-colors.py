class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = [0] * 3

        for el in nums:
            freq[el] += 1

        i = 0
        for val in range(3):
            while freq[val] > 0:
                nums[i] = val
                i += 1
                freq[val] -= 1