class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight = 0
        l, r = 0, len(heights)-1
        for i in range(0, len(heights)):
            if l < r:
                height = heights[l] * abs(l-r)
                if maxHeight < height:                    
                    maxHeight = height
                l += 1
            else:
                height = heights[r] * abs(l-r)
                if maxHeight < height:
                    print(l, r)
                    maxHeight = height
                r -= 1
        return maxHeight