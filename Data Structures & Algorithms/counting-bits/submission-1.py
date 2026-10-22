class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        dp = {}
        def count1Bits(n):
            counter = 0
            while n > 0:
                if n & 1 == 1:
                    counter+=1
                n = n>>1
                

            return counter

        for i in range(0, n+1):
            if i//2 in dp:
                lostBit = i & 1
                dp[i] = dp[i//2] + lostBit
            else:
                dp[i] = count1Bits(i)
            res.append(dp[i])
        return res

        