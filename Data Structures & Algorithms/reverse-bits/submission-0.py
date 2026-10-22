class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            lastBit = n & 1
            n = n >> 1
            if lastBit == 1:
                res = res * 2 + 1
            else:
                res= res*2
        return res
