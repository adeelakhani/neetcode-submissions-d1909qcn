import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculateEatingRate(eatingRate, piles):
            totalHours = 0
            for i in piles:
                totalHours+=math.ceil(i/eatingRate)
            return totalHours

        maxTime = max(piles)
        minTime = 1
        l, r = minTime, maxTime
        res = 0
        while l<=r:
            mid = l+(r-l)//2
            hoursTaken = calculateEatingRate(mid, piles)
            if hoursTaken > h: # took too many hours, need to increase eating rate
                l = mid+1
            elif hoursTaken < h: # took too few hours, can try to decrease eating rate in hopes to find a better solution
                r = mid - 1
                if hoursTaken > res:
                    res = mid
            else:
                return mid
        return res


        