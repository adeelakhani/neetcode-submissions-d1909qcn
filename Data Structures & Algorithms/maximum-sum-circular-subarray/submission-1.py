class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currSumMin = 0
        currSumMax = 0
        maxSum = nums[0]
        minSum = nums[0]
        for n in nums:
            currSumMin = min(currSum, 0)
            currSumMax = max(currSum, 0)
            currSumMin += n
            currSumMax += n
            minSum = min(currSumMin, minSum)
            maxSum = max(currSumMax, maxSum)
        return max(
            sum(nums)-minSum,
            maxSum
            )