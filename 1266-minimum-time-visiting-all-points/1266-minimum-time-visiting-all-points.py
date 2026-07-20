class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(0, len(points)-1):
            x1, y1, x2, y2 = points[i][0], points[i][1], points[i+1][0], points[i+1][1]

            ans += max(abs(x1-x2), abs(y1-y2))

        return ans