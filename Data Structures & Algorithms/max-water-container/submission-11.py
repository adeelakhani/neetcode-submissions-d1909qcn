class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lptr, rptr = 0, len(heights)-1
        maxHeight = 0
        while lptr < rptr:
            height2 = self.calculateArea(heights[lptr], heights[rptr], rptr-lptr)
            if height2 > maxHeight:
                maxHeight = height2
            if heights[lptr] < heights[rptr]:
                lptr += 1
            else:
                rptr -=1
        return maxHeight
    def calculateArea(self, a:int, b:int, dis:int) -> int:
        area = min(a,b) * dis
        return area