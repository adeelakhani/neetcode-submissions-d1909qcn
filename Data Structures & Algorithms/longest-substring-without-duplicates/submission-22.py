class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = float('-inf')
        currLength = 0
        l = 0
        window = set()
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                currLength -=1
                l+=1
            window.add(s[r])
            currLength +=1
            res = max(res, currLength)
        return res

