class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]: return -1
        queue = collections.deque()
        queue.append((0,0))
        visited = set()
        visited.add((0,0))
        length = 1
        while queue:

            for i in range(0,len(queue)):
                r, c = queue.popleft()
                if (r,c) == (n-1, n-1):
                    return length
                neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1], [1,-1], [1,1], [-1,-1],[-1,1]]
                for dr, dc in neighbors:
                    if min(r+dr,c+dc)<0 or r+dr==n or c+dc == n or (r+dr,c+dc) in visited or grid[r+dr][c+dc] == 1:
                        continue
                    
                    queue.append((r+dr,c+dc))
                    visited.add((r+dr, c+dc))
            length+=1
        return -1
                