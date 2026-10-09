class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        def dfs(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0

        for r in range(0,ROWS):
            for c in range(0, COLS):
                if grid[r][c] == 1:
                    print(r,c)
                    islands = dfs(r,c)
                    print(islands)
                    if islands > maxArea:
                        maxArea = islands

        return maxArea



