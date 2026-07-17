class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for i in range(1, rows):
            grid[i][0] += grid[i-1][0]

        for j in range(1, cols):
            grid[0][j] += grid[0][j-1]

        for i in range(1, rows):
            for j in range(1, cols):
                top = grid[i][j-1]
                left = grid[i-1][j]

                grid[i][j] += min(top, left)

        return grid[-1][-1]