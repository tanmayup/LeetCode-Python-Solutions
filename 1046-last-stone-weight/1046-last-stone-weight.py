class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # while len(stones) > 1:
        #     stones.sort()
        #     stones[-1], stones[-2] = stones[-1] - stones[-2], 0
        #     stones.remove(0)

        # return stones[0]

        import heapq

        h = []
        for stone in stones:
            heapq.heappush(h, -stone)

        while len(h) > 1:
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)

            heapq.heappush(h, y-x)

        return -heapq.heappop(h)