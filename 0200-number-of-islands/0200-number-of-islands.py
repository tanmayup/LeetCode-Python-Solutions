class Solution:
    def remove_neighbours(self, grid, i, j):
        if i == -1 or i == len(grid) or j == -1 or j == len(grid[0]):
            return

        # if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        #     return

        if grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.remove_neighbours(grid, i+1, j)
        self.remove_neighbours(grid, i-1, j)
        self.remove_neighbours(grid, i, j+1)
        self.remove_neighbours(grid, i, j-1)


    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.remove_neighbours(grid, i, j)

        return count