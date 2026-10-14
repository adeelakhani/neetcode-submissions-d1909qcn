class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = set()
        path = []
        def dfs(i, path):
            if i == len(nums):
                res.add(tuple(path.copy()))
                return
            

            dfs(i+1, path)
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()
        
        dfs(0, path)
        return [list(t) for t in res]