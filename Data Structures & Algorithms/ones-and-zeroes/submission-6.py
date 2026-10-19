class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:




        cache = {}
        def memoization(i,zeroes,ones):
            if i == len(strs):
                return 0
            
            if (i,zeroes,ones) in cache:
                return cache[(i,zeroes,ones)]

            num0, num1 = strs[i].count('0'), strs[i].count('1')
            if zeroes-num0 < 0 or ones-num1 < 0:
                cache[(i,zeroes,ones)] = max(0, memoization(i+1, zeroes, ones))
            else:
                cache[(i,zeroes,ones)] = max(1 + memoization(i+1, zeroes-num0, ones-num1), memoization(i+1, zeroes, ones))

            return cache[(i,zeroes,ones)]
        return memoization(0, m, n)