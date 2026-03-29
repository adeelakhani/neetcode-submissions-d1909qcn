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
        # array: [1,2,4,6]
        # prefix: [1, 2, 8, 48] multiply each number left to right so index 1 (2) is 1*2 
        # postfix: [48, 48, 24, 6] multiply each number right to left so index 2 (4) is 4*6
        # basically at each index
        # the index before it on the prefix is the stuff multiplied upto it(the numbers before it)
        # the index after it, is the stuff multiplied after it(the rest of the numbers after it) 
        # so multiplying these 2 literally gives all the numbers multiplied before and after it!
            
        