class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "$" + s
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        strs = []
        # i = s[0]
        i = 0
        while i < len(s):
            # if s[i].isdigit():
            # length = int(s[i])
            length = ""
            for j in range(i, len(s)):
                char = s[j]
                print("char " + char)
                if char == "$":
                    break
                length += char
            print("length", length)
            length = int(length)
            newWord = ""
            for j in range(1, length+1):
                newWord += s[j]
            strs.append(newWord)
            i += length + 1 
        return strs
