class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        prev = [0] * COLS
        for i in range(ROWS-1, -1, -1):
            curr = [0] * COLS
            if i == ROWS-1:
                curr[-1] = 1
            else:
                curr[-1] = prev[-1]
            for j in range(COLS-1, -1, -1):
                if j != COLS-1:
                    curr[j] = curr[j+1] + prev[j]
                
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
            prev = curr
        
        return prev[0]