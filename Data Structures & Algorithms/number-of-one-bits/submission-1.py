class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n > 0:
            lastDigit = n & 1
            n = n>>1
            if lastDigit == 1:
                total +=1
        return total