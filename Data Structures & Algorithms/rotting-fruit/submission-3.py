class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        startR, startC = 0,0
        totalOnes = 0
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(0,ROWS):
            for j in range(0,COLS):
                if grid[i][j] == 2:
                    startR,startC = i, j
                elif grid[i][j] == 1:
                    totalOnes += 1
        if grid[startR][startC] != 2:
            return -1
        queue = collections.deque()
        queue.append((startR,startC))
        grid[startR][startC] = 2
        length = -1

        while queue:
            for i in range(0,len(queue)):
                r, c  = queue.popleft()
                neighbours = [[1,0],[-1,0],[0,-1],[0,1]]
                for dr, dc in neighbours:
                    if min(r+dr, c+dc) < 0 or r+dr == ROWS or c+dc == COLS or grid[r+dr][c+dc] in (0,2):
                        continue
                    
                    queue.append((r+dr, c+dc))
                    grid[r+dr][c+dc] = 2
                    totalOnes -=1

            length+=1
        

        return length if totalOnes == 0 else -1
