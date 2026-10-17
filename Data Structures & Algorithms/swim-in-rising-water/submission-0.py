class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = {}
        ROWS, COLS = len(grid), len(grid[0])
        minheap = [(grid[0][0], (0,0))]

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in res:
                continue
            
            if n1[0] == ROWS-1 and n1[1] == COLS-1:
                return w1
            res[n1] = w1

            neighbors = [[1,0], [-1, 0], [0,1], [0,-1]]
            for dr, dc in neighbors:
                r = n1[0] + dr
                c = n1[1] + dc
                if r < 0 or c < 0 or r == ROWS or c == ROWS:
                    continue
                if (r, c) not in res:
                    heapq.heappush(minheap, (max(grid[r][c], w1), (r, c)))
        
        print(res)
        i, j = max(res, key=res.get)
        return grid[i][j]

