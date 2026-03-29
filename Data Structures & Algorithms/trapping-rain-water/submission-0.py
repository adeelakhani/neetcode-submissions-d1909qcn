class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r, maxLeft, maxRight = 0, len(height)-1, height[0], height[len(height)-1]
        total = 0
        while l < r:
            if(maxLeft < maxRight):
                l+=1
                maxLeft = max(maxLeft, height[l])
                total += maxLeft - height[l]
            else:
                r-=1
                maxRight = max(maxRight, height[r])
                total += maxRight - height[r]
        return total
            

