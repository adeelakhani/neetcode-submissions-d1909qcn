class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0
        l, r = 0, 0
        length = 0 
        # (r-l)+1
        hashSet = set()
        # hashSet.add(s[l])
        # for c in s:
            # hashSet.add(c)
        while r<=(len(s)-1):
            if s[r] in hashSet:
                while s[l] != s[r]:
                    l+=1
                l+=1
                hashSet.clear()
                if (r-l) > length:
                    length = r-l
                print(s[l], s[r])
                print(l, r)
            else:
                hashSet.add(s[r])
                if (r-l) > length:
                    length = r-l
                r+=1
                print(s[l], s[r])
                print(l, r)

        return length
            # go thru array
            # if we can add one more to the substring, r++
            # keep adding and check each time if its greater than current length
            # btw add the current char to a set so we can search in o(1) for duplicates
            # if the one we add is in alr, then l is the new one, r l+1