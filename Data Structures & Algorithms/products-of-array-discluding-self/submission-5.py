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
        postfix = postfix[::-1]

        print(prefix)
        print(postfix)
            
        