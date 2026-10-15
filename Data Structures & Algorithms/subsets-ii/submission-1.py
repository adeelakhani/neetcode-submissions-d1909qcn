class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []
        nums.sort()
        def dfs(i, path):
            if i == len(nums):
                res.append(path.copy())
                return
            [1,2,2,2]
            
            path.append(nums[i])
            dfs(i+1, path)
            
            path.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1, path)
            
            
        
        dfs(0, path)
        return res



        # nums.sort()
        # res = set()
        # path = []
        # def dfs(i, path):
        #     if i == len(nums):
        #         res.add(tuple(path.copy()))
        #         return
            

        #     dfs(i+1, path)
        #     path.append(nums[i])
        #     dfs(i+1, path)
        #     path.pop()
        
        # dfs(0, path)
        # return [list(t) for t in res]