class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        h = []
        import heapq
        for el in d:
            heapq.heappush(h, (d[el], el))

            if len(h) > k:
                heapq.heappop(h)

        return [el for (freq, el) in h]