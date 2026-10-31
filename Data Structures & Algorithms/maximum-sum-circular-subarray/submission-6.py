class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currSumMin = 0
        currSumMax = 0
        maxSum = nums[0]
        minSum = nums[0]
        for n in nums:
            currSumMin = min(currSumMin, 0)
            currSumMax = max(currSumMax, 0)
            currSumMin += n
            currSumMax += n
            minSum = min(currSumMin, minSum)
            maxSum = max(currSumMax, maxSum)

        return max(nums) if max(nums) < 0  else max(sum(nums)-minSum, maxSum)