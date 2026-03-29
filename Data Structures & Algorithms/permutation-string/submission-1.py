from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l, r = 0, len(s1)-1

        hashMap = defaultdict(int)
        tempHashMap = defaultdict(int)
        for c in s1:
            hashMap[c] += 1
        while r < len(s2):
            for i in range(l, r+1):
                tempHashMap[s2[i]] += 1
            if hashMap == tempHashMap:
                return True
            else:
                tempHashMap = defaultdict(int)
                l+=1
                r+=1
        return False

