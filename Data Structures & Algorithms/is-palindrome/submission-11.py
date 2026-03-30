class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        left, right = 0, len(s) - 1
        palindrome = True
        while left <= right:
            if not self.isAlphanumeric(s[left]):
                left+=1
            elif not self.isAlphanumeric(s[right]):
                right-=1
            else:
                if s[left].lower() != s[right].lower():
                    palindrome = False
                left+=1
                right-=1

    def isAlphanumeric(self, c) -> bool:
        if (48 <= ord(c) <= 57) or (65 <= ord(c) <= 90) or (97 <= ord(c) <= 122):
            return True
        return False

