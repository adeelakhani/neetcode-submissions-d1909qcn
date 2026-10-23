class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        neighbours = [[1,0], [-1,0], [0,1], [0,-1]]
        pacific = (
            {(0, col) for col in range(len(heights[0]))} 
            | {(row, 0) for row in range(1, len(heights))}
            )
        atlantic = (
            {(len(heights)-1, col) for col in range(len(heights[0]))} 
        | {(row, len(heights[0]) - 1) for row in range(1, len(heights))}
        )

        

        def dfs(row, col, visited):
            if (row, col) in visited:
                return
            visited.add((row, col))
            for [dr,dc] in neighbours:
                if row+dr == ROWS or col+dc == COLS or row + dr < 0 or col + dc < 0 or heights[row][col] > heights[row+dr][col+dc]:
                    continue
                
                dfs(row+dr, col+dc, visited)

        
        visitedPacific = set()
        # go through all pacific nodes:
        for row, col in pacific:
            dfs(row, col, visitedPacific)
        visitedAtlantic = set()
        # go trhough all atlatntic nodes:
        for row, col in atlantic:
            dfs(row, col, visitedAtlantic)
        print(visitedAtlantic)

        return list(visitedPacific & visitedAtlantic)
        
