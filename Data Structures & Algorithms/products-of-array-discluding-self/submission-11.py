class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        for i in nums:
            total *= i
        print(total)
        output = len(nums) * [total]
        for i in range(0, len(nums)):
            output[i] = output[i]/nums[i]

        return output
        