class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight = 0
        l, r = 0, len(heights)-1
        for i in range(0, len(heights)):
            height = heights[l] * heights[r]
            if maxHeight < height:
                maxHeight = height
            if l < r:
                left +=1
            else:
                r -= 1
        return maxHeight