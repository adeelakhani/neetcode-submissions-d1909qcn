from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r=0,0
        tFreq = defaultdict(int)
        windowFreq = defaultdict(int)
        sl, sr = 0, float('inf')
        # rule of thumb, if valid then shift until invalid, else shift right(when invalid)
        for c in t:
            tFreq[c]+=1
        while r < len(s):
            windowFreq[s[r]] +=1
            r+=1
            while self.isValid(tFreq, windowFreq):
                if r-l < sr-sl:
                    sr = r
                    sl = l
                windowFreq[s[l]] -= 1
                l+=1
        return s[sl:sr+1] if sr != float('inf') else ""

    def isValid(self, tFreq, windowFreq):
        isV = True
        for k,v in tFreq.items():
            if tFreq[k] > windowFreq[k]:
                isV = False
                break
        return isV

            