class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxR = 0

        for i in range(len(heights)):
            index = i
            while stack and stack[-1][0] > heights[i]:
                height, index = stack.pop()
                if (i - index) * height > maxR:
                    maxR = (i - index) * height
            stack.append((heights[i], index))
        
        fullwidth = len(stack)
        for height, index in stack:
            if (fullwidth - index) * height > maxR:
                maxR = (fullwidth - index) * height
        return maxR