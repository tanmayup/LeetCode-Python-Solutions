# class Solution(object):
#     def findKthLargest(self, nums, k):
#         for _ in range(k-1):
#             maxnum = max(nums)
#             nums.remove(maxnum)
#         return max(nums)

class Solution(object):
    def findKthLargest(self, nums, k):
        # nums.sort()
        # return nums[(-1)*k]

        import heapq
        h = []
        for el in nums:
            heapq.heappush(h, el)
            if len(h) > k:
                heapq.heappop(h)

        return h[0]