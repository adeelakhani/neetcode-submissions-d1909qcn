class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverseS = ""
        newS = s.replace(" ", "")
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                reverseS += s[i]
        print(reverseS)
        if reverseS == s:
            return True
        else:
            return False
