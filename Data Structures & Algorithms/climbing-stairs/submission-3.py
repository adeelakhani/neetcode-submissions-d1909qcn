class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def memoization(n):
            if n <= 2:
                return n

            if n in cache:
                return cache[n]
            
            cache[n] = memoization(n-1) + memoization(n-2)
            return cache[n]
        
        return memoization(n)