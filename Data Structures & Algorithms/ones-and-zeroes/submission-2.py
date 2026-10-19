class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # at most m zeroes
        # at most n ones
        cache = {}
        def memoization(i,zeroes,ones):
            if i == len(strs) or zeroes < 0 or ones < 0:
                return 0
            
            if (i,zeroes,ones) in cache:
                return cache[(i,zeroes,ones)]

            num0, num1 = self.calculate1s0s(strs[i])
            cache[(i,zeroes,ones)] = max(1 + memoization(i+1, zeroes-num0, ones-num1), memoization(i+1, zeroes, ones))
            return cache[(i,zeroes,ones)]
        return memoization(0, m, n)



    
    def calculate1s0s(self, s: str) -> List:
        numZeros = 0
        numOnes = 0
        for c in s:
            if c == '0':
                numZeros +=1
            if c == '1':
                numOnes += 1
        return [numZeros, numOnes]