class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, length = 0, 0
        hashSet = set()
        for r in range(0, len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l+=1
            hashSet.add(s[r])
            if (r-l) > length:
                length = r-l
        return length
        # if len(s) == 1:
        #     return 1
        # elif len(s) == 0:
        #     return 0
        # l, r = 0, 0
        # length = 0 
        # hashSet = set()
        # while r<=(len(s)-1):
        #     if s[r] in hashSet:
        #         while s[l] != s[r]:
        #             l+=1
        #         l+=1
        #         hashSet.clear()
        #         if (r-l) > length:
        #             length = r-l
        #         print(s[l], s[r])
        #         print(l, r)
        #     else:
        #         hashSet.add(s[r])
        #         if (r-l) > length:
        #             length = r-l
        #             print(hashSet)
        #             print("HERE UPDATING", length)
        #         print(s[l], s[r])
        #         print(l, r)
        #         r+=1
        # return length
