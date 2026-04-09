class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for(int i = 0; i < nums.length(); i++)
        l, r = 1, max(piles)
        # piles: [1, 6, 2, 3, 8]
        # min to max: [1, 2, 3, 4, 5, 6, 7, 8]
        # h = 5
        # l = 1
        # r = 8
        k = float('inf')
        while l <= r:
            mid = l + (r-l)//2
            hrsTaken = 0
            for i in piles:
                hrsTaken += math.ceil(i/mid)
            # so in this case lets say that k = 4, h is 5, the hours it took is 7
            if hrsTaken > h:
                l = mid + 1
            else:
                if mid < k:
                    k = mid
                r = mid - 1
        return k


                





        