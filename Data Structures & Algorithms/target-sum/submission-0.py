class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        def memoization(i, total):
            
            if i == len(nums):
                if total == target:
                    return 1
                return 0

            return memoization(i+1, total-nums[i]) + memoization(i+1, total+nums[i])

        return memoization(0, 0)