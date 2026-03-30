class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, r = 0, len(nums)-1
        # 3, 3, 1, 4, 6
        nums.sort()
        print(nums)
        # for num in nums:
