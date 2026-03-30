class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # racecar
        # carrace
        # {
        #     r: 2,
        #     a: 2,
        #     c: 2,
        #     e: 1
        # }
        # lettersS[]
        lettersS = {}
        lettersT = {}
        for i in range(len(s)):
            lettersS[s[i]] = lettersS.get(s[i], 0) + 1
            lettersT[t[i]] = lettersT(t[i], 0) + 1

        if lettersS != lettersT:
            return False
        else:
             return True  