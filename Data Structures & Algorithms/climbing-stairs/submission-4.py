class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        
        dp = [1, 2]
        i = 3
        while i <= n:
            temp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = temp
            i+=1
        return dp[1]
        
        
        
        # cache = {}
        # def memoization(n):
        #     if n <= 2:
        #         return n

        #     if n in cache:
        #         return cache[n]
            
        #     cache[n] = memoization(n-1) + memoization(n-2)
        #     return cache[n]
        
        # return memoization(n)