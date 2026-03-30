from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        d = deque()
        l = r = 0
        # you have a new element comming in, if nums[r] > deque[-1] (rightmost element
        # is smaller than the new element so breaks monotonically decreasing) thus we 
        # pop the right side. then we add our new guy
        # then we wanna ensure the left side is also in the proper range
        # then(only if r >= k-1, we've gone as far as fill up initial window since we
        # dont wanna record max if youve only filled up 2 elements lol and k = 3 initially)
        # we will record the max

        
        while r < len(nums):
            while d and nums[r] > nums[d[-1]]:
                d.pop()
            d.append(r)

            if d[0] < l:
                d.popleft()
            
            if r >= k-1:
                ans.append(nums[d[0]])
                l+=1
            r+=1
        return ans