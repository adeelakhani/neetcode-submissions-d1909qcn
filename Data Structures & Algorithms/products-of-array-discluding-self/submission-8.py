class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #basically we multiple all numbers left to right and right to left[watch vid it'll make sense lowk]
        postfix=[]
        prefix=[]
        multiplier = 1
        for i in range(0, len(nums)):
            multiplier *= nums[i]
            prefix.append(multiplier)
        multiplier = 1
        for i in range(len(nums)-1, -1, -1):
            multiplier *= nums[i]
            postfix.append(multiplier)
        postfix = postfix[::-1] # start:end:step
        result = []
        for i in range(0, len(nums)):
            if i == 0:
                result.append(postfix[i+1])
            elif i == (len(nums)-1):
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1] * postfix[i+1])
        return result
        print(prefix)
        print(postfix)
            
        