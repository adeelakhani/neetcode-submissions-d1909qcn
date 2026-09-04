class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (0, 1):
            return 1
        elif n < 0:
            return 0
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)