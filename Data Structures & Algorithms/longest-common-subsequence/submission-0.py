class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = {}
        def memoization(t1i, t2i, cache):
            if t1i == len(text1) or t2i == len(text2):
                return 0
            if ((t1i, t2i) in cache):
                return cache[(t1i, t2i)]
            elif text1[t1i] == text2[t2i]:
                cache[(t1i, t2i)] = 1 + memoization(t1i+1, t2i+1, cache)
                return cache[(t1i, t2i)]

            cache[(t1i, t2i)] = max(memoization(t1i+1, t2i, cache), memoization(t1i, t2i+1, cache))
            return cache[(t1i, t2i)]
        
        return memoization(0, 0, cache)
            