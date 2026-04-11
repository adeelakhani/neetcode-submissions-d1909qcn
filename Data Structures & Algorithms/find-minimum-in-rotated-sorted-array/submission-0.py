class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minimum = float('inf')
        # [2, 3, 4, 5, 6, 1]
        while l<=r:
            mid = l + (r-l) // 2
            if nums[mid] < minimum:
                minimum = nums[mid]
            if nums[r] < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return minimum


# example cases:
        # over here we do a binary search, 
        # mid is 5. so in the middle, if we look nums[l] and nums[r]
        # so we can see 2 < 5 and 3 < 5 but the SMALLER one is l
        # so we make our new l = 2 + 1 = nums[3] = 6
        # now mid is 1, so we do 
        # [3,4,5,6,1,2]
        # [1,2,3,4,5,6]
        # [3, 4, 5, 0, 2]