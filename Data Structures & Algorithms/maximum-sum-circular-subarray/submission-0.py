class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]
        for n in nums:
            currSum = min(currSum, 0)
            currSum += n
            maxSum = min(currSum, maxSum)
        return sum(nums)-maxSum