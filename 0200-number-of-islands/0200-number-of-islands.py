class Solution:
    ans = 0
    def scan(self, grid, i, j):
        rows = len(grid)
        cols = len(grid[0])

        if i < 0 or i >= rows or j < 0 or j >= cols:
            return

        if grid[i][j] == "0":
            return

        grid[i][j] = "0"

        self.scan(grid, i+1, j)
        self.scan(grid, i-1, j)
        self.scan(grid, i, j+1)
        self.scan(grid, i, j-1)


    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    self.scan(grid, i, j)

        return count