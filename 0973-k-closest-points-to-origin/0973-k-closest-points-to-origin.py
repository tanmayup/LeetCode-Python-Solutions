class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        h = []
        import heapq
        for (x, y) in points:
            dist = -(x*x + y*y)
            heapq.heappush(h, (dist, x, y))

            if len(h) > k:
                heapq.heappop(h)

        return [(x, y) for (dist, x, y) in h]