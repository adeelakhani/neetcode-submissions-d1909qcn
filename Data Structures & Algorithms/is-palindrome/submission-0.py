class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverseS = ""
        for i in range(len(s)-1, -1, -1):
            reverseS += s[i]
        if reverseS == s:
            return True
        else:
            return False
