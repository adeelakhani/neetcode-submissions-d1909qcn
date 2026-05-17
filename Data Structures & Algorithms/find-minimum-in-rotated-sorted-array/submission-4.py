class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minSF = float('inf')
        if nums[l] < nums[r]:
            return nums[l]
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                if minSF > nums[mid]:
                    minSF = nums[mid]
                r = mid-1
        return minSF