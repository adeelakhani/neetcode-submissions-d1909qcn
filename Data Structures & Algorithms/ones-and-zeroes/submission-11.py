class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = defaultdict(int)

        for i in range(len(strs)):
            s = strs[i]
            zeroes = s.count('0')
            ones = s.count('1')
            for M in range(0, m+1):
                for N in range(0, n+1):
                    if M - zeroes < 0 or N - ones < 0:
                        dp[(i, M, N)] = dp[(i-1, M, N)]
                    else:
                        dp[(i, M, N)] = max(dp[(i-1, M, N)], 1 + dp[(i-1, M - zeroes, N - ones)])

        return dp[(len(strs)-1,m,n)]



        # cache = {}
        # def memoization(i,zeroes,ones):
        #     if i == len(strs):
        #         return 0
            
        #     if (i,zeroes,ones) in cache:
        #         return cache[(i,zeroes,ones)]

        #     num0, num1 = strs[i].count('0'), strs[i].count('1')
        #     if zeroes-num0 < 0 or ones-num1 < 0:
        #         cache[(i,zeroes,ones)] = max(0, memoization(i+1, zeroes, ones))
        #     else:
        #         cache[(i,zeroes,ones)] = max(1 + memoization(i+1, zeroes-num0, ones-num1), memoization(i+1, zeroes, ones))

        #     return cache[(i,zeroes,ones)]
        # return memoization(0, m, n)