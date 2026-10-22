class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        def count1Bits(n):
            counter = 0
            while n > 0:
                if n & 1 == 1:
                    counter+=1
                n = n>>1
                

            return counter

        for i in range(0, n+1):
            res.append(count1Bits(i))
        return res

        