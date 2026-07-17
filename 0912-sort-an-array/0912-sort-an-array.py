class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    #     return self.mergesort(nums)
    # def mergesort(self, arr):
    #     if len(arr) <= 1:
    #         return arr

    #     mid = len(arr) // 2
    #     l = arr[:mid]
    #     r = arr[mid:]

    #     l = self.mergesort(l)
    #     r = self.mergesort(r)

    #     return list(self.merge(l, r))

    # def merge(self, l, r):
    #     ans = []

    #     while len(l) != 0 and len(r) != 0:
    #         if l[0] < r[0]:
    #             ans.append(l[0])
    #             l.remove(l[0])

    #         else:
    #             ans.append(r[0])
    #             r.remove(r[0])

    #     if len(l) == 0:
    #         ans = ans + r
    #     else:
    #         ans = ans + l

    #     return ans

        mn = min(nums)

        for i in range(len(nums)):
            nums[i] = nums[i] - mn

        freq = [0] * (max(nums) + 1)

        for el in nums:
            freq[el] += 1

        sort = []

        for i in range(max(nums)+1):
            while freq[i] > 0:
                sort.append(i)
                freq[i] -= 1

        for i in range(len(sort)):
            sort[i] = sort[i] + mn

        return sort