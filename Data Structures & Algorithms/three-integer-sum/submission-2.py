class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, r = 0, len(nums)-1
        # 3, 3, 1, 4, 6
        nums.sort()
        for i in range(0, len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                l = i + 1
                while l <= r:
                    if (nums[i] + nums[l] + nums[r]) == 0:
                        return True
                    elif (nums[i] + nums[l] + nums[r] < 0):
                        l+=1
                    else:
                        r+=1
        return False
