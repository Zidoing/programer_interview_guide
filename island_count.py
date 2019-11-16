



grid = [["0","1","0"],
        ["1","0","1"],
        ["0","1","0"]]

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        r = len(grid)
        c = len(grid[0])
        count = 0
        for row in range(r):
            for col in range(c):
                if grid[row][col] == '1':
                    count += 1
                    self.infect(r, c, row, col, grid)
        return count

    def infect(self, r, c, row, col, grid):
        if row >= r or r < 0 or col >= c or col < 0 or grid[row][col] != '1':
            return
        grid[row][col] = '2'
        self.infect(r, c, row + 1, col, grid)
        self.infect(r, c, row - 1, col, grid)
        self.infect(r, c, row, col + 1, grid)
        self.infect(r, c, row, col - 1, grid)



print(Solution().numIslands(grid))