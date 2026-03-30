class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + s
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        strs = []
        # i = s[0]
        for i in range(0, len(s)):
            # if s[i].isdigit():
            print(s[i])
            break
            length = int(s[i])
            newWord = ""
            for j in range(1, length+1):
                newWord += s[j]
            strs.append(newWord)
            i+=length
        return strs
