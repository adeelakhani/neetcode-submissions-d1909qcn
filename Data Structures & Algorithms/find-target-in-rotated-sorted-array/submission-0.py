class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[r]: # section 1
                if nums[mid] < target:
                    l = mid+1
                else: # nums[mid] > target, not equal cus if it was it would be caught earlier
                    if nums[l] <= target < nums[mid]:
                        r = mid-1
                    else:
                        l = mid+1
            else: # section 2
                if target > nums[mid]:
                    if nums[mid] <= target <= nums[r]:
                        l = mid + 1
                    else:
                        r= mid - 1
                else:
                    r = mid - 1
        return -1

