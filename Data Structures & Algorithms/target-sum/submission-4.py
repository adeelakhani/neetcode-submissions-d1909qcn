class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = [defaultdict(int) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        prev = dp[0]
        for i in range(0, len(dp)-1):
            for k,v in dp[i].items():
                dp[i+1][k+nums[i]] += dp[i][k]
                dp[i+1][k-nums[i]] += dp[i][k]
        
        return dp[len(nums)][target]



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