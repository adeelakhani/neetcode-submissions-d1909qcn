class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i,j)]
            if i == len(nums1) or j == len(nums2):
                return 0

            cache[(i,j)] = max(dfs(i + 1, j),dfs(i, j + 1), dfs(i + 1, j+1))
            return cache[(i,j)]

        return dfs(0, 0)

