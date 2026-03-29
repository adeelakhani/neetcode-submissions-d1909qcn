class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = {}
        x2 = {}
        l, r = 0, len(s1)-1
        for s in s1:
            x[s] = x.get(s, 0) + 1
        while r <= len(s2)-1:
            for i in range(l,r+1):
                s = s2[i]
                x2[s] = x2.get(s, 0) + 1
            l+=1
            r+=1
            if x == x2:
                return True
            x2 = {}
        return False