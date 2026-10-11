class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2,1,1,100]
        # [2, 2]
        if len(nums) < 2:
            return nums[0]

        dp = [nums[0], max(nums[1],nums[0])]
        
        i = 2
        while i < len(nums):
            tmp = dp[1]
            dp[1] = max(dp[1], dp[0] + nums[i])
            dp[0] = tmp
            i+=1

        return dp[1]