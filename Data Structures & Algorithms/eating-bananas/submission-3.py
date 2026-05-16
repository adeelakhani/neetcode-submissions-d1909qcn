import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k range = 1 to len(piles)
        l, r = 1, max(piles)
        trackMinK = -299
        while l <= r:
            mid = l+(r-l)//2
            h_try = self.calculateHoursGivenK(piles, mid)
            if h_try > h: # if my h i got given my k is too high, it takes too long to eat thus i try a larger eating rate
                l = mid+1
            elif h_try < h:
                r = mid-1
                trackMinK = mid
            else:
                return mid
        return trackMinK

    def calculateHoursGivenK(self, piles:List[int], k: int) -> int:
        total = 0
        for i in piles:
            total += math.ceil(i/k)
        return total


        # l = 1, r = max(piles)
        # binary search from l = 1, r = max(piles)
        # function will take in a k and give a h, if that 
        # [25,10,23,4]
        # 1 -> 25, mid = 12
        # array[mid] -> 