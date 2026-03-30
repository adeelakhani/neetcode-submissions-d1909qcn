class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight = heights[0] * heights[len(heights)-1]
        l, r = 0, len(heights)-1
        for i in range(0, len(heights)):
            if l < r:
                height = heights[l] * heights[l]
                if maxHeight < height:
                    maxHeight = height
                l += 1
            else:
                height = heights[r] * heights[r]
                if maxHeight < height:
                    maxHeight = height
                r -= 1
        return maxHeight