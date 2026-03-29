class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        backwards = ""
        forwards = ""
        counter = 0
        for i in range(len(s)-1, -1, -1):
            if self.isAlphanumeric(str(s[i])):
                backwards += s[i].lower()
            if self.isAlphanumeric(str(s[counter])):
                forwards+=s[counter].lower()
            counter +=1
            
        if forwards == backwards:
            return True
        else:
            return False
        
    def isAlphanumeric(self, c: str) -> bool:
        if (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
            return True
        else:
            return False

