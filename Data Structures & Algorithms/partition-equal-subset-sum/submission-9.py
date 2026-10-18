class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum%2:
            return False
        target = totalSum/2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            if target in dp:
                return True
            nextDP = set()
            for val in dp:
                nextDP.add(val + nums[i])
                nextDP.add(val)
            dp = nextDP
        return True if target in dp else False

        
        
        
        
        
        # cache = {}
        # totalSum = sum(nums)
        # if totalSum%2 == 1:
        #     return False
        # target = totalSum/2
        
        # def memoization(i, remainingTarget):
            
        #     if (i, remainingTarget) in cache:
        #         return cache[(i, remainingTarget)]
        #     if remainingTarget == 0:
        #         return True
            
        #     if i == len(nums) or remainingTarget < 0:
        #         return False

        #     cache[(i, remainingTarget)] = memoization(i+1, remainingTarget) or memoization(i+1, remainingTarget-nums[i])

        #     return cache[(i, remainingTarget)]
        
        # return memoization(0, target)
                