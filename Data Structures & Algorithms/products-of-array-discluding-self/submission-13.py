class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i-1]
        for i in range(len(nums)-1, -1, -1):
            if i == (len(nums)-1):
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i] * postfix[i+1]
        output = []
        for i in range(0, len(nums)):
            if i == 0:
                output[i] = prefix[i+1]
            if i == len(nums):
                output[i] = prefix[i-1]
            else:
                output[i] = prefix[i-1] * postfix[i+1]

        return output