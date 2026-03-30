class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        lettersS = {}
        lettersT = {}
        for letter in s:
            lettersS[letter] = lettersS[letter] + 1
        for letter in t:
            lettersT[letter] = lettersT[letter] + 1
        if lettersS != lettersT:
            return False
        else:
             return True  