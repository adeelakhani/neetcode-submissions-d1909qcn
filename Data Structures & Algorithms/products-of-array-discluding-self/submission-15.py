class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        increasing = [1] * len(nums)
        decreasing = [1] * len(nums)

        dc = len(nums)-1
        for i in range(len(nums)):
            if i > 0:
                increasing[i] = nums[i] * increasing[i-1]
                decreasing[dc] = nums[dc] * decreasing[dc+1]
            else:
                increasing[i] = nums[0]
                decreasing[dc] = nums[-1]
            dc-=1
        res = []
        for i in range(len(nums)):
            if i-1 < 0:
                res.append(decreasing[i+1])
            elif i+1 == len(nums):
                res.append(increasing[i-1])
            else:
                res.append(increasing[i-1] * decreasing[i+1])
        return res


