class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        grid=[
        ["1","1","0","0","1"],
        ["1","1","0","0","1"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]

        '''
        def dfs(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        ROWS, COLS = len(grid), len(grid[0])
        total_islands = 0


        for i in range(0, ROWS):
            for j in range(0, COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    total_islands+=1
        
        return total_islands

            
            