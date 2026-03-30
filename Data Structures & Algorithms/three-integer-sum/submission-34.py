class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                if a + nums[l] + nums[r] == 0:
                    result.append([a, nums[l], nums[r]])
                    l+=1
                elif a + nums[l] + nums[r] < 0:
                    l+=1
                elif a + nums[l] + nums[r] > 0:
                    r-=1
        return result