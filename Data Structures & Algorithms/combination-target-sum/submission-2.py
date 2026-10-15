class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

            path = []
            res = []
            def dfs(i):
                if sum(path) == target:
                    res.append(path.copy())
                    return
                
                if sum(path) > target:
                    return

                for j in range(i, len(nums)):
                    path.append(nums[j])
                    dfs(j)
                    path.pop()
            dfs(0)
            return res

            
            
            
            # the reason we have startindex is: when we do it for the 2's we find every
            # possible combination regarding 2, so we dont want to include 2 in the every
            # possible combination regarding 3, that is how we avoid duplciates