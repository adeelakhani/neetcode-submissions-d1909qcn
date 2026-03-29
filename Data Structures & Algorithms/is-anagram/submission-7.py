class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict1={}
        myDict2={}
        for i in range(len(s)):
            myDict1[s[i]] = myDict1.get(s[i], 0) + 1
        for i in range(len(t)):
            myDict2[t[i]] = myDict2.get(t[i], 0) + 1

        return myDict1==myDict2
