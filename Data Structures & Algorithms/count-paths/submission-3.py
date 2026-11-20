class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[1]*m for _ in range(n)]
        for i in range(1, len(arr)):
            for j in range(1, len(arr[0])):
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
        
        return arr[n-1][m-1]