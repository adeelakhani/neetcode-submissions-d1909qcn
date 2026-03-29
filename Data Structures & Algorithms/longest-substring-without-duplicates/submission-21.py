class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 0
        yo = set()
        yo.add(s[0])
        longest =0 
        while r < len(s):
            longest = max(longest, (r-l)+1)
            r+=1
            if r < len(s) and s[r] in yo:
                while s[r] in yo:
                    yo.discard(s[l])
                    l+=1
            if r < len(s):
                yo.add(s[r])
        longest = max(longest, r-l)
        return longest

