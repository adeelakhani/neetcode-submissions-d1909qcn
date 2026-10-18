class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = set()
        dp.add(0)
        total = 0
        for i in range(len(nums)):
            nextdp = set()
            for t in dp:
                if i == len(nums)-1:
                    if t+nums[i] == target:
                        total+=1
                    if t-nums[i] == target:
                        total+=1
                else:
                    nextdp.add(t+nums[i])
                    nextdp.add(t-nums[i])
            dp = nextdp
        return total




        # cache = {}
        # def memoization(i, total):
            
        #     if (i, total) in cache:
        #         return cache[(i, total)]
        #     if i == len(nums):
        #         if total == target:
        #             return 1
        #         return 0

        #     cache[(i, total)] = memoization(i+1, total-nums[i]) + memoization(i+1, total+nums[i])
        #     return cache[(i, total)]

        # return memoization(0, 0)