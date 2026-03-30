class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, r = 0, len(nums)-1
        # 3, 3, 1, 4, 6
        newNums = nums.sort()
        print(newNums)
        # for num in nums:
