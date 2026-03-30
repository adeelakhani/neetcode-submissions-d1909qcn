class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        left, right = 0, len(s) - 1
        palindrome = True
        while left <= right:
            if not isAlphanumeric(s[left]):
                left+=1
            elif not isAlphanumeric(s[right]):
                right+=1
            else:
                if s[left].lower() != s[right].lower():
                    palindrome = False

    def isAlphanumeric(self, c) -> bool:
        if (48 <= ord(c) <= 57) or (65 <= ord(c) <= 90) or (97 <= ord(c) <= 122):
            return True
        return False

