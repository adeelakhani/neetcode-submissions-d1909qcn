class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        
        
        
        
        cache = {}
        if sum(nums)%2 == 1:
            return False
        target = sum(nums)/2
        
        def memoization(i, remainingTarget):
            
            if (i, remainingTarget) in cache:
                return cache[(i, remainingTarget)]
            if remainingTarget == 0:
                return True
            
            if i == len(nums) or remainingTarget < 0:
                return False

            cache[(i, remainingTarget)] = memoization(i+1, remainingTarget) or memoization(i+1, remainingTarget-nums[i])

            return cache[(i, remainingTarget)]
        
        return memoization(0, target)
                