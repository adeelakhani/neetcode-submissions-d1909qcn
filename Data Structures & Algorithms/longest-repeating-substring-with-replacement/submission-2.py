from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r,l = 0,0
        d = defaultdict(int)
        ans = 0
        
        while r < len(s):

            d[s[r]] += 1
            maxChar = 0
            for key,v in d.items():
                maxChar = max(maxChar, v)
            while r-l+1 - maxChar > k:
                d[s[l]] -=1
                l+=1
            ans = max(ans, r-l+1)
            r+=1
        return ans
