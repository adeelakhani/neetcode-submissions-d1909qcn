class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
        def memoization(i, total):
            
            if (i, total) in cache:
                return cache[(i, total)]
            if i == len(nums):
                if total == target:
                    return 1
                return 0

            cache[(i, total)] = memoization(i+1, total-nums[i]) + memoization(i+1, total+nums[i])
            return cache[(i, total)]

        return memoization(0, 0)