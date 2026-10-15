class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(i, path):
            if len(path) == k:
                res.append(path.copy())
                return
            
            if i > n:
                return
            path.append(i)
            dfs(i+1, path)
            path.pop()
            dfs(i+1, path)

        dfs(1, path)
        return res

        
        
        
        
        
        
        
        
        # n choose k way
        # path = []
        # res = []
        # def dfs(i, path):
        #     if len(path) == k:
        #         res.append(path.copy())
        #         return
        #     # optional check
        #     if i > n:
        #         return
            
        #     for i in range(i, n+1):
        #         path.append(i)
        #         dfs(i+1, path)
        #         path.pop()
        
        # dfs(1, path)
        # return res
            

